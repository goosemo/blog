---
title: Using the parallel branch of Fabric
date: 2011/01/06 18:50:48
categories: Programming
tags: python, fabric, multiprocessing, job_queue
reddit: Python
---

Changes and Notes
-----------------

So I've updated the branch to have add in a useful bit for it's use. I also
need to talk out a few things related to it's use in the environment and some 
bugs or hiccups one might run into trying to use it. Hopefully I'll be hitting
this up some more soon, and pulling some more of the crazy cool updates that
people have been making to fabric trunk. I have a to-do list, let me know if you
want me to add anything to it!

Additional feature
==================

So there's always been a flag to make the pool size of the bubble, and that was
nice, but I wanted a way to make these more permanent as well as simpler to
remember. So it's now an option in the runs_parallel decorator. To use it you'd
just simply give it a size to use:

.. code-block:: python

    #!/usr/bin/env python

    from fabric.api import *

    env.hosts = ['host%2d.com' % x for x in range(20)]

    @runs_parallel(with_bubble_of=10)
    def poke():
        run('uptime')


This I feel makes a cleaner fabfile, and puts this information where it should
be, in the code, and out of the writer's head.

How to use both ways, or just one
=================================

A big thing to note in using parallel tasks, is that anything put into shared
variables, like env, is **forgotten** outside the execution of the one instance of
the task. So if you don't add a @runs_once or @runs_sequential decorator to a
task that say sets the env.hosts before an actual parallel task, the work done
inside the env setting task is forgotten. 

The reason adding these decorators addresses this, is that by adding them, the 
task isn't executed using the parallel bits. It is instead run inside the main 
fab process, and isn't creating a fork pool of size 1 and forgetting about it 
when the fork is finished executing.

So as an example, if one were to try and run a fabfile w/o setting up
decorators for their functions, and running: *fab -P set_hosts uptime*

.. code-block:: python

    #!/usr/bin/env python

    from fabric.api import env, local, run, sudo

    env.hosts = ['somehost.com']

    def set_hosts():
        env.hosts = ['web-0', 'web-1']

    def uptime():
        run('uptime')

They'd get into an issue where the set_hosts not being specifically set to run
sequential or once, would have the settings it made to the env.hosts var only
apply inside the task, since it's been forked out. Which would cause the uptime
to only run on somehost.com, and not both web-0 and web-1 as expected.

Fixing it
~~~~~~~~~

To get around this the tasks that need to set variable globally, and affect
other tasks later will need to be decorated to not use forking. Below is the
same fabfile tweaked to do so, as well as explicitly state how functions should
behave. 

Note that setting up a task to *@runs_once* will be backwards compatible,
but *@runs_parallel* isn't. The added benefit to this being that one can drop
using the *-P* flag, as neither task in this example can switch hit.

.. code-block:: python

    #!/usr/bin/env python

    from fabric.api import *

    #thanks to Eric who pointed this out, visit his site, it's neat
    env.hosts = ['ericholscher.com']

    @runs_once
    def set_hosts():
        env.hosts = ['web-0', 'web-1']

    @runs_parallel
    def uptime():
        run('uptime')

Maybe it'll help
================

As a boon to people using both the parallel branch and Trunk, on a single
fabfile, note that which one is being used can be determined at runtime using
some silly introspection:

.. code-block:: python

    >>> from fabric import decorators
    >>> dir(decorators)
    ['StringTypes', '__builtins__', '__doc__', '__file__', '__name__',
    '__package__', '_parallel', '_sequential', 'hosts', 'is_parallel',
    'is_sequential', 'needs_multiprocessing', 'roles', 'runs_once',
    'runs_parallel', 'runs_sequential', 'wraps']
    >>> "runs_once" in dir(decorators)
    True

So one could just flip a Boolean and decorate/use things accordingly. Though I
suggest using @runs_once on any tasks that are just that, single shots that do
stuff local, or set vars for the fabfile, and to reserve using @runs_sequential
for tasks that still need to have multiple hosts, but need to not run side by
side.


Bug outstanding
===============

Finally there is a outstanding bug with use of this branch on windows,
https://github.com/goosemo/fabric/issues#issue/5, that'll bite people. I'll try
and work this out, but I'm a bad developer and am dragging my feet on having to
install windows to debug this. But it's the new year so I'll make it a
resolution, and we all know people never drop those.


**I've updated this a bit since the first push of the post**
