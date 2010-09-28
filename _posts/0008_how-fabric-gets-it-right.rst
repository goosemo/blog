---
categories: Linux, Programming, Tools
date: 2010/02/11 00:56:33
guid: http://morgangoose.com/blog/?p=76
permalink: http://morgangoose.com/blog/2010/02/how-fabric-gets-it-right/
tags: python, fabric, pyohio, rst
title: How fabric gets it right
---

I like fabric_. A lot.
----------------------

Its a easy to use tool that continually makes my life simpler, and my projects smarter and more automated. Not much out there can really say that. At least nothing I use daily, without noticing, and dependably.

I used to use vellum, and that did what I needed. But fabric being under active development, and getting new features each version it seems is a huge plus. That and it does the network stuff for you, along with the nitty gritty.

Recently I have been giving presentations to the `Ohio State University's Open Source Club <http://opensource.osu.edu/>`_ about `gnu tools <http://morgangoose.com/p/gnu_tools/>`_, `python tools <http://morgangoose.com/p/tool_oriented_python/>`_, and soon some cli apps. Fabric really helped make this simple for me to get a whole system down for making and uploading these.

I made all of those presentations in restrctured text, and compiled them into their final formats. All of which was scripted in fabric. I became really attached to ReST after getting introduced to it watching `Catherine Devlin <http://catherinedevlin.pythoneers.com/>`_ give a `talk about restructured text <a href="http://catherinedevlin.pythoneers.com/presentations/rst/olf.html>`_ at Ohio Linux Fest. I ended up finding a cool rst2s5 command that makes nice presentations and with a little tweaking it now also has syntax highlighted code blocks, and can make nice pdfs.

In starting to use fabric you'll notice the basic idea is that you'd make a fabfile that works a lot like a Makefile or a SConstruct file would, with make and scons respectively. You'll make calls with the fab command in the directory the fabfile is located and it will supply the targets.

Below in this example, two targets are made, pack and deploy. The pack target will just makes a tarball, using the local function fabric provides. The deploy target calls pack to make this tarball, then using the put function will place the tarball into the tmp directory, then change into the web dir provided, and extract the archive. It knows automaticly to do this to both hosts I provided, and since I am using an ssh key does all this trickery autonomously.

:fabfile.py:  

.. code-block:: python

    from fabric.api import *

    env.user = 'username'
    env.hosts = ['host1.com', 'host2.com']

    def pack():
        local('tar czf /tmp/project_foo.tgz project_foo/', capture=False)

    def deploy():
        pack()
        put('/tmp/project_foo.tgz', '/tmp/')

        with cd('/var/www/foo/'):
            run('tar xzf /tmp/project_foo.tgz')


Fabric can do a lot more than just deploy
-----------------------------------------

It's docs_ have a lot of detail, and explain most everything well. A last example of some a cool fabric config would be the one I use to publish my presentations to this site.

:fabfile.py:  

.. code-block:: python

    from fabric.api import *

    env.roledefs = {
        'production': ["morgangoose.com"],
        }


    def setup_vars(project):    
        global presentation
        global presentation_archive
        global rst_source
        global pdf

        project = project.strip("/")
        presentation = project
        presentation_archive = "%s.tar.gz" % presentation
        rst_source = "%s.rst" % presentation
        pdf = "%s.pdf" % presentation

    @roles('production')
    def upload(project):
        env.user = "username"
        p_dir = "/var/www/html/p/"
    
        package(project)
        put(presentation_archive, p_dir)
        put("%s/%s" % (presentation, pdf), p_dir)
        with cd(p_dir):
            run("rm -rf %s/" % presentation)
            run("tar zxvf %s" % presentation_archive)
    
        local("rm -f %s" % presentation_archive)        
    
    def package(project):
        setup_vars(project)
        make_presentation()
        local("tar zcvf %s %s" % (presentation_archive, presentation))
    
    def make_presentation():
        #PDF first
        local("rst2pdf %s/%s -o %s/%s" % (
            presentation, rst_source, presentation, pdf, ))
    
        #Then s5 html presentation
        local("python rst-directive.py \
                --stylesheet=pygments.css \
                --theme=small-black \
                --quiet \
                %s/%s > %s/index.html" % (
                    presentation, rst_source, presentation, ))
    
    def new(project):
        setup_vars(project)
        local("mkdir -p %s/{,files}" % presentation)
        local("cp -R ui %s/" % presentation)
        local("touch %s/%s" % (presentation, rst_source))
    
    
This has some more complicated bits, where it uses the role decorator to specify only to use the hosts listed in the production role definitions. 

It also takes advantage of an awesome feature I didn't know fabric had where, one can send arguments to a fabric target. So the project parameter in the targets here can be, and is, supplied via the command line. 


For example
-----------

I used this to deploy the updates to my most recent presentation:

.. code-block:: bash

    $ fab upload:tool_oriented_python


That's telling fabric to run the upload target, and send the string "tool_oriented_python" as an argument to the function. 

If you forget the targets you have just do:

.. code-block:: bash

    $ fab -l


.. _fabric: http://docs.fabfile.org
.. _docs: fabric_
