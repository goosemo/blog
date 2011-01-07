---
title: Using the parallel branch of Fabric
date: 2011/01/06 18:50:48
categories: Programming
tags: python, fabric, multiprocessing, job_queue
reddit: Python
---

So I've updated the branch to have add in a useful bit for it's use. I also
need to talk out a few things related to it's use in the environment and some 
bugs or hiccups one might run into trying to use it.

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

A big thing to note in using parallel tasks, is that anything put into shared
variables, like env, is forgotten outside the execution of the one instance of
the task. So if you don't add a @runs_once or @runs_sequential decorator to a
task that say sets the env.hosts before an actual parallel task, the work done
inside the env setting task is forgotten. The reason adding these decorators
addresses this, is that by adding them, the task isn't executed using the
parallel bits. It is instead run inside the main fab process, and isn't 
creating a fork pool of size 1 and forgetting about it when the fork is 
finished executing.

So if as an example, this will set the hosts and then execute the task in
parallel when run as: fab stage push

.. code-block:: python

    #!/usr/bin/env python

    from fabric.api import env, local, run, sudo

    #thanks to Eric who pointed this out, visit his site, it's neat
    env.hosts = ['ericholscher.com']

    @runs_once
    def set_hosts():
        env.hosts = ['web-0', 'web-1']

    @runs_parallel
    def uptime():
        run('uptime')


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

Finally there is a outstanding bug with use of this branch on windows,
https://github.com/goosemo/fabric/issues#issue/5, that'll bite people. I'll try
and work this out, but I'm a bad developer and am dragging my feet on having to
install windows to debug this. But it's the new year so I'll make it a
resolution, and we all know people never drop those.


