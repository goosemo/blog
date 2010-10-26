---
categories: Linux, Servers
date: 2009/07/22 17:15:23
guid: http://morgangoose.com/blog/?p=43
permalink: http://morgangoose.com/blog/2009/07/trac-makes-my-life-easy/
tags: apache, trac, bitten, python
author: Morgan Goose
title: Trac makes my life easy
---
The project management app Trac_ is something that was new to me a while back. I'd just installed t for a side project, and used the yum install without any issues. It took care of all the grunt work, and got me to the point where I could now create and use a trac project.

Trac is set up like what I see web frameworks go with. A main program that will install the framework in a project directory. In this case trac-admin , which is killer when you want to make multiple projects, and offers a cli interface to the project s framework configuration, etc.

This setup becomes awesome I found when you want to upgrade. Yum installed what it had packaged, the .10 version, but I had decided that I wanted to toy with bitten_ their automated build tool, which required .11 and up. So an upgrade was needed, yum couldn t be used, but I found that trac-admin has an upgrade command.

So I was poised to make the fun and scary transition into mixing a package managed install with a source install, not something that always goes well. I ve found that sometimes packagers change to install location from where the src install goes (looking at you nagios), and make some conflicts or at least confusion.

The upgrade process for the server then my app was as simple as:

.. code-block:: bash

    wget http://ftp.edgewall.com/pub/trac/Trac-0.11.5.tar.gz
    tar zxvf http://ftp.edgewall.com/pub/trac/Trac-0.11.5.tar.gz
    cd Trac-0.11.5
    python setup.py install
    trac-admin /path/to/project upgrade
    trac-admin /path/to/project wiki upgrade
    /etc/init.d/httpd restart

This blew me away. I ve have never had a complicated app (relativily of course) upgrade so simply, and without any issues. The main install of trac from empty folder to working project manager was simple too, so perhaps I should have expected this, but really I think it is a testimony to how well the developers of Trac have though of the whole process of using their framework.

.. _Trac: http://trac.edgewall.org
.. _bitten: http://bitten.edgewall.org
