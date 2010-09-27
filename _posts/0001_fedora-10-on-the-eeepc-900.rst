---
categories: Linux
date: 2009/05/04 19:22:09
guid: http://morgangoose.com/blog/?p=5
permalink: http://morgangoose.com/blog/2009/05/fedora-10-on-the-eeepc-900/
tags: fedora, woot, eeepc
title: Fedora 10 on the eeePC 900
---
Recently got the woot.com deal on the eeepc 900, sans webcam. I tried to use the xanadros os that was bundled with it for a few days, but the lack of normal gnu tools and normal packages made me want to switch. So I decided to to look into putting my os of choice fedora onto it.

**Installing:**

Found that is was a dooable_ project_, exciting and surprising.  Since the netbook doesn't have a dvd-rom drive, and I lent out my external, I decided to go the usb live stick route.

Directions_ for this were easy to find, I did have to use the command line version of them, and found through trial and error that only my name brand Kingston drive would get the netbook to boot.

To get the usb drive to boot, hit escape while booting or hit f2 and set the main drive to be the usb drive.  After it boots and finishes and installs, everything pretty much works.

When I brought up the machine I started to follow `Gavin's_directions`__ and run a general update. This failed, only because it filled the small hard drive up. I then had to find the /var/cache/yum/updates/packages/ directory and clear it by hand, because yum didn't have the room to run and remove the rpms itself.

**Removing things to make space:**

So now I had to sleuth around to find out what was taking up all the space on the drive. Using 

.. code-block:: bash

    du -Hs -si /*

found that the largest folder in the root dir was usr. And walking down that path structure I found that the three largest folders, that I could do something about, were:

	* /usr/share/locale @332MB
	* /usr/share/doc @106MB
	* /usr/share/fonts @223MB

So I really went through and removed a whole lot of this stuff, which depending on ones needs, may not be advisable.

I removed all fonts that could using yum instead of just deleting them, as that just really seemed like a bad idea. It took a bit of grep'ing, so this line is a little long, but it basically strips out all the extra fonts, and keeps liberation as well as core font tools and libs. I personally use Anonymous, for all my coding, and terminal work, and I put that in .fonts dir, so really even this is a bit liberal for me.

.. code-block:: bash

    rpm -qa | grep font \
    | grep -ve'xorg' -ve'core' -ve'liberation' -ve'fontconfig' -ve'lib' -ve'bitmapfonts' -ve'ghostscript' \
    | xargs yum -y erase

Note also that this removes these apps:

	* gimp
	* abiword
	* evince
	* ghostscript (even though I tried not to)

This frees up most of the 200MB that the fonts dir takes up, so we're off to a good start.

The locale directory I was unfamiliar with, but some searching found that this is where data for other language support is stored. I only speak one, and found that removing these doesn't cause irreparable harm. So delete them I did.  Since these are installed with every program, and the language packs don't have their own RPMs yum wasn't useful in this case.

.. code-block:: bash
    
    ls /usr/share/locale/* -d \
    | grep -ve'locale.alias' -ve'default' -ve'en' \
    | xargs rm -rf

This frees up about another 300MB. But it is also something that will crop up again, since any new program you install will add it own locale information. For apt-get there is a nice plug-in that will automatically strip out this information for you on install, but in my shallow searching for this for yum there didn't seem to be a substitute. Might be a good weekend project.

The share doc directory I just cd'ed into and wiped out its contents. This is a netbook, and I can ssh into my home machine to read those if I need to, so I freed up another 100 or so MB with this wipe.

This brings us a lot closer to a good 1 GB of free space. I went further and removed a few apps I won't be using:

	* evolution
	* rhythmbox
	* cheese

**Now to try and get the services under control.**

Found this great listing_ of what each service does, so if you're unsure if you want to stop as many as I chose to, look it up and make sure. I also chose to use the command line service conf tool: 

.. code-block:: bash

    /sbin/chkconfig  --list 
    
So its a bit time consuming but I went through the chkconfig list and grepped out the 5:on states and checked them against my list below and set them to off one at a time for every run time level.  There might be a quicker way, but I couldn't think of one that didn't involve making a script, so I let it be, and stuck with manual.

	* cron, atd, anacron
	* auditd (also disabled SELinux)
	* avahi-daemon
	* bluetooth
	* btseed, bttrack
	* capi
	* cups[*]
	* firstboot
	* ip6tables
	* irda
	* irqbalance
	* isdn
	* kerneloops
	* lm_sensors
	* mdmonitor
	* multipathd
	* netconsole
	* netfs
	* nfs
	* nfslock
	* nmbd
	* nscd
	* pcscd
	* portreserve
	* restorecond
	* rpcbind
	* rpcgssd*
	* sendmail
	* smb
	* ypbind

Now not all of those services were up, but I just made the list of what I would remove, and didn't take note of what was not running in that list.

Then I installed my must haves: xfce, vim, htop, all the dvcs', tilda, and tomboy. I rsync'ed over my dot dirs that I wanted, and I was good.


.. _dooable: http://fedoraproject.org/wiki/EeePc#Eee_PC_90x.2F1000_Series
.. _project: http://idolinux.blogspot.com/2009/02/fedora-10-on-eee-pc-1000.html
__ project_ 
.. _Directions: http://fedoraproject.org/wiki/FedoraLiveCD/USBHowTo
.. _listing: http://www.mjmwired.net/resources/mjm-services-f10.html
