---
categories: Linux, Programming
date: 2009/07/22 17:26:42
guid: http://morgangoose.com/blog/?p=45
permalink: http://morgangoose.com/blog/2009/07/decouple-with-kwargs/
tags: python, kwargs, optparse, mutliprocessing
title: Decouple with kwargs
---
So I've been attempting to make a suite of cli scripts for work. I recently discovered the multiprocessing_ module for python, and really liked its simplicity, and started using it, with great success. Everything was faster.

This then spurred me to take the scripts that were for the most part, copy common-ish bits and then modify to suite, and turn them into a library of sorts. The neat part then arose when I wanted to import a argument parser, as well as pass off to a proc creation component.  

In doing this I had in mind that the 'script' would need to only define a function to make a list of commands to run on a given server, and a __main__ section that would pass in a list of servers, the function to make a command list and some other info. This way the script itself would only be two definition sections, and only the parts that were going to be unique for the most part.

The problem that came up in doing this is when I wanted the function that makes the command list to have more arguments that normal. How would I pass them in, and how would I define them so that I don't have to edit my libraries to accommodate this argument passing.  It was kwargs that saved me there, that and some optparse_ tweaking.

Here is a basic example:

**script.py**

.. code-block:: python

    def get_commands(host, **kwargs):
        command_list = []
    
        user = kwargs['user']
        key_file = kwargs['key_file']

        command_list.append("echo %s" % user)

        return command_list    

    if __name__ == '__main__':
        import automation

        hosts = []

        (hosts, options) = automation.process_args(sys.argv)

        automation.thread_hosts(
                hosts,
                get_commands,
                options,
                user="test"
                )


**automation.py** (library w/ functions)

.. code-block:: python

    def thread_hosts(hosts, get_commands, options={}, **kwargs):
        import multiprocessing
 
        kwargs.update(options)

        jobs = []
    
        for host in hosts:
            p = multiprocessing.Process(
                    target=run_commands, 
                    args=(
                        host,
                        get_commands(host, **kwargs),
                        ), )

            jobs.append(p)
            p.start()


So this example is a script that defines the function to return a command list, and provides an options var, and list of hosts. The thread hosts then loops over the hosts each time  passing the host and the get_commands function to another library function that connects to said host, and loops over the returned command list.

A part that might be confusing is that the parse_args function returns optparse's options variable but the options.__dict__ representation specifically. This then allows me to be able to update kwargs with any options that I allow to be set at the command line. The example in the script being the key_file variable.

The neat part of all this is being able to take the kwargs for one function and pass it right along to the next. This is key, because it allows for the library function in this case to be able to be entirely decoupled from the script itself. 

With this implementation I am able to write a script that defines extra args to use, and only the script need know what they are. In the examples the library will just dumbly pass them along in the kwargs dict, I never have to tell it that I want to pass a user variable to it, and it makes the script a nice self contained unit.

.. _multiprocessing: http://docs.python.org/library/multiprocessing.html
.. _optparse: http://docs.python.org/library/optparse.html
