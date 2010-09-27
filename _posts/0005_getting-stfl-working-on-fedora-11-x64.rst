---
categories: Linux
date: 2009/07/30 11:14:11
guid: http://morgangoose.com/blog/2009/07/getting-stfl-working-on-fedora-11-x64/
permalink: http://morgangoose.com/blog/2009/07/getting-stfl-working-on-fedora-11-x64/
tags: ''
title: Getting stfl working on fedora 11 x64
---
Newbeuter_ is my preferred way to browse RSS feeds. Its a great CLI app that is 'Mutt Of Feed Readers', and being a user of mutt_ I love this app for being so similar. I wanted to use the newest version of newbeuter, because recently I have been on a kick to get all of my apps: screen, vim, mutt, and now newsbuter; setup with 256 colours.

I read on the development blog that the newest version in the git repo was able to use 256 colours, so I immediately cloned the repo and started the install process. I was stopped immediately at the config.sh. It wanted the stfl libraries and wasn't able to find them, and neither could yum.

Looking into the config.sh I saw that it was querying pkg-config for the flags to use on compilation to see if the library was present. It wasn't, and so I also read further on the notes for the git repo version, and saw the bit about using the latest svn copy of stfl. So I checked that out, made it and installed it onto my machine. But this didn't get me any further into making newsbueter, because pkg-config was still unable to find libstfl.

So I decided to try and figure out what the issue was with stfl and pkg-config. First thing I saw was that the stfl.pc file that pkg-config uses to make its responses was in the wrong place for my system. It was in /usr/local/lib/pkgconfig, instead of with the other libraries on my system in /usr/lib64/pkgconfig. This resolved the issue of pkg-config not knowing where the pc file for stfl was, and pkg-config was now returning actual data about libstfl. A recompilation of newsbeuter did show that there was still a problem. I now received: error while loading shared libraries: libstfl.so.0: cannot open shared object file: No such file or directory.

I did another updatedb, and ran a locate for all stfl files, and found that the make install for stfl was putting the libs in a strange place as well. I then updated both the Makefile.cfg and the stfl.so.in to reflect the locations of other libs:

**Makefile.cfg** changed lines

.. code-block:: make

    export libdir ?= lib64
    export prefix ?= usr 
    export DESTDIR ?= /  


**stfl.pc.in** changes lines

.. code-block:: make

    prefix=/usr
    exec_prefix=/usr
    libdir=/usr/lib64
    includedir=/usr/include


This got me pretty far I think, because now the system looked like the other libraries. The stfl.pc lines were taken almost verbatim from the sqlite3.pc file in fact. I was still getting the shared library issue though, and after not thinking about the problem for a bit I realized that the stfl makefile had made libstfl.so.0.21 and the error message was not able to find libstfl.so.0, so I too the logical leap and made a symlink named libstfl.so.0 that pointed to libstfl.so.0.21 in the /usr/lib64/ directory. After making sure that this worked, I made a change to the makefile for stfl, and added another line to make a second symlink, that ended in 0:

**Makefile**

.. code-block:: make

    ln -fs libstfl.so.$(VERSION) $(DESTDIR)$(prefix)/$(libdir)/libstfl.so.0


I do admit that there may be a better way to do this, and some of it may be done with command line config or make flags. I don't know them, and was able to successfully build with these changes.

.. _Newbeuter: http://www.newsbeuter.org
.. _mutt: http://www.mutt.org 
