---
title: Parallel execution with fabric
date: 2010/10/08 19:00:15
categories: Programming
tags: python, fabric, multiprocessing, job_queue
---

It's been a wish for some for a long time
-----------------------------------------

Since at least `07/21/2009 <http://code.fabfile.org/issues/show/19>`_ the 
desire to have fully parallel execution across hosts, or something similar to 
that.  I stumbled upon the thread around March of this year.  Being that I'd 
been using Fabric_ for a number of months at this point, and had recently made 
a script set for work stuff that leveraged multiprocessing_ I decided to give 
the issue a go.

.. _Fabric: http://docs.fabfile.org
.. _multiprocessing: http://docs.python.org/library/multiprocessing.html

What I implemented, and why
---------------------------

The short of it being that I made a data structure, Job_Queue_ that I feed fab
tasks into and it will keep a running 'bubble' (works like a pool) of 
multiprocessing Processes going executing the Fabric_ tasks as they are able 
to do so. The job queue having a pool size as set by the user, or 1/2 the size
of the host list if not specified, or if the pool size is larger than the host
list size, it will match the host list size.

.. _Job_Queue: http://github.com/goosemo/job_queue

Why not threads?
================

Because they won't do what I want parallel execution in Fabric_ to accomplish.
Namely

* I can't be sure that the task is not IO bound as users can call anything
  as it 'just python', and the GIL will trip up fully parallel tasks.

* With threads there is an issue noted in the docs about `importing in threaded 
  code`_ which is something a user of Fabric_ is more than welcome to do.

* The need for inter-process communication isn't there. Tasks are by their
  nature encapsulated, and don't talk to one another when being run.

.. _importing in threaded code: http://docs.python.org/library/threading.html#importing-in-threaded-code

OK so why not X instead?
========================

There seems to have been a glut of good work done recently in the python
ecosystem on getting around the issues people are having with the GIL. Some
names that I can recall being Twisted_, Tornado_, pprocess_, and PP_. I am 
sure there are a lot more. There also the neat looking execnet_ project that
offers direct communication to a python interpreter over an open socket.

.. _Twisted: http://twistedmatrix.com/documents/current/core/howto/threading.html
.. _Tornado: http://www.tornadoweb.org/documentation#low-level-modules
.. _pprocess: http://www.boddie.org.uk/python/pprocess.html
.. _PP: http://www.parallelpython.com/
.. _execnet: http://codespeak.net/execnet/

Those got tossed out because they each have something that causes them to not
fit some or all three requirements I gave modules to use.

* Cross platform Win/Mac/Linux

* Works on Python 2.5+

* Is in the stdlib

All of those fail the last requirement, and granted it perhaps wouldn't be hard
to get users to install yet another dep, but it is best to avoid things like
that if at all possible. Keeps the moving parts down, and the issues you have
to debug less foreign. Note though that the other two criteria I set could
actually be met by any in list above, I am writing this much removed from my
initial decision process.

So forks, why create a new Queue/Pool?
======================================

Trickery.

The multiprocessing_ module has a lot of really nice builtins that I attempted
to leverage, but there really just wasn't a way to do what I needed to do with
them. Queue was nice for having a list of Processes, but I needed a worker
pool. Pool provided this, but then the workers were anonymous, and I wasn't
able to set names as a cheap way to keep track of which host it was to run on.

So I had to make something up. That's what Job_Queue_ is for. All it does if
take a load of Processes and then when the job queue is closed, one starts it,
and off it goes. It'll make a bubble of a certain size that it will keep the
number of currently running forks under, and will just move that bubble along
the internal queue it had from the loading.

So it looks a bit like this::

    ---------------------------
    [-----]--------------------
    ---[-----]-----------------
    ---------[-----]-----------
    ------------------[-----]--
    --------------------[-----]
    ---------------------------


The trickery comes in when in the fabric job_queue.py I set the job.name of the
Process to the host, and inside the queue I leverage this with::

    env.host_string = env.host = job.name
    job.start()
    self._running.append(job)

Which will set the host for the task at run time, since otherwise Fabric_ would
have gotten confused. It would have continued to iterate the same host, because
of the shared state env and it's host list isn't really able to be progressed,
because the forks aren't sharing it anymore, and are instead working in
isolation from one another. 

While that could have been a reason to use threads, or something like the
Manager that multiprocessing_ offers, it's really the only time it comes up,
and it keeps things a lot simper at the moment. Not to say that if someone is
convincing enough I'd probably get behind a more robust solution.

What this branch adds to Fabric
--------------------------------

There are new command flags for fab::

    -P, --parallel        use the multiprocessing module to fork by hosts
    -z FORKS, --pool-size=FORKS Set the number of forks to use in the pool.

I have also added two decorators::

    @runs_parallel
    @runs_sequential

These will allow a fab file command to be set to be run either in parallel or
sequentially regardless of the fab command flag. Without these commands switch 
when the flag is set.

What that means is that any tasks that are decorated are always run as either
parallel or sequential. Tasks that omit these decorators though, are going to
be able to switch back and forth between running parallel or running
sequentially. Something the user would be specifying at run time with the -P
flag.

With the new stuff comes a few caveats
--------------------------------------

If you are interested in the guts, the implementation is in the main.py file,
and uses the Job_Queue class in the job_queue.py file. Note that this is only
implemented in the fab command, as there is no way to determine how one will 
execute functions if they are using Fabric as a helper library.

If the runs_once decorator is being used on a function that is called from
inside a fabric task, it won't be able to be honored. Because the states in the
forks are separate, and every fork will think it's the first one to run the
function. Simple solution being to make the call it's own task call.

Now to see it in use
--------------------

Here is a little example of a fab file that is running some command on the
server that will take 10 seconds to run. Yeah sleep is a bit of cheat for this,
but it's good enough to show the benefit of forking out tasks that'd take a
crap ton of time otherwise

.. code-block:: python

    from fabric.api import *
    from server_list import servers

    env.roledefs = servers.server_classes

    @roles('servers')
    def poke():
        run("sleep 10")


Running it
==========

In parallel, as specified on the cli. Note that this is an example of not in 
using the decorators to set this in the code, so it as a task/function can 
toggle between being run in parallel or sequentially.

.. code-block:: bash

    $ time fab poke -P -z 20
    ...

    real   0m45.868s
    user   1m7.928s
    sys    0m8.425s


Now the long runner. It takes ... forever.

.. code-block:: bash

    $ time fab poke
    ...

    real   8m51.477s
    user   6m3.239s
    sys    1m26.637s


The difference is pretty dramatic. We get a 8 min fab task dropped down to less
than one min.

Just cause I though it was neat
===============================

This is a glimpse of what it'll look like in the process tree. Those are the 
forks running their tasks, and the children under them are the threads that 
bitprophet_ added into Fabric_ core for greatly improved stream handling.

.. _bitprophet: http://github.com/bitprophet

.. code-block:: bash

    $ pstree -paul
    ...
    │   ├─bash,20062
    │   │   └─fab,21455 /home/mgoose/.virtualenvs/fabric-merge/bin/fab poke -P -z 20
    │   │       ├─fab,21462 /home/mgoose/.virtualenvs/fabric-merge/bin/fab poke -P -z 20
    │   │       │   └─{fab},21493
    │   │       ├─fab,21463 /home/mgoose/.virtualenvs/fabric-merge/bin/fab poke -P -z 20
    │   │       │   ├─{fab},21484
    │   │       │   ├─{fab},21505
    │   │       │   ├─{fab},21511
    │   │       │   └─{fab},21517
    │   │       ├─fab,21464 /home/mgoose/.virtualenvs/fabric-merge/bin/fab poke -P -z 20
    │   │       │   └─{fab},21487
    │   │       ├─fab,21465 /home/mgoose/.virtualenvs/fabric-merge/bin/fab poke -P -z 20
    │   │       │   ├─{fab},21483
    │   │       │   ├─{fab},21502
    │   │       │   ├─{fab},21503
    │   │       │   └─{fab},21504
    ...
    (16 more fab lines)


Use it and let me know
----------------------

I'd love to hear how people are using this, and if they find any holes in my
implementation. I've got a few more things I want/need to add into this, and
I've got them listed in the `github issues`_ just until this gets integrated
into the Fabric_ mainline.

.. _github issues: http://github.com/goosemo/fabric/issues
