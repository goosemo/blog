---
categories: Linux, Servers
date: 2010/06/02 22:52:43
guid: http://morgangoose.com/blog/2010/06/fedora-kvm-with-simple-netowrk-forward/
permalink: http://morgangoose.com/blog/2010/06/fedora-kvm-with-simple-network-forwards/
tags: bash, iptables, fedora, kvm
author: Morgan Goose
title: Fedora KVM with simple network forwards
---
Recently I've been teaching python to some high school students. It has been going well, but the development environment we had access to left a little bit to be desired. We were working with ages old solaris, vi only, and no real access to newer gnu (or other) tools. So a new setup was required, I went off to investigate.

I started with chroot, since a buddy, Daniel Thau, had used it extensively for running `multiple operating systems side by side <http://opensource.osu.edu/sites/default/files/chroottalk_0.pdf>`_. He'd pointed me in the directions of `febootstrap <http://people.redhat.com/~rjones/febootstrap/>`_ and that seemed like it'd work fine. I was able to make a sandbox, get ssh running on 2022 and then have my dlink route that to my box. Success!

But I found that a bit messy, and a bit limited. I wanted to lock down how much of my resources they could use, and I didn't want to have to give access to some of my root file systems directly; /proc, /dev, etc. So I looked around a bit more, and stumbled on using KVM indirectly via the new virt-manager toolset that fedora 12 and 13 provide. Installation was as simple as:

.. code-block:: bash

    $ yum install qemu-kvm virt-manager virt-viewer python-virtinst


But it also seems that from the `techotopia article <http://www.techotopia.com/index.php/Installing_and_Configuring_Fedora_KVM_Virtualization>`_ I followed for some of this that one could also just do:

.. code-block:: bash

    $ yum groupinstall 'Virtualization'


I have to say it's a pretty swank set of tools. It's free, it works on KVM or Xen. KVM usage requires no special kernel and as such, no reboot. The setup was simple, and gave out a vnc port to connect to from the get go. It is also trivial to connect to a setup on machine A with virt-manager on machine B over ssh. If you want more information, `fedora has a nice writeup <http://fedoraproject.org/wiki/Virtualization_Quick_Start>`_, and libvirt has a more `distro agnostic set of docs <http://wiki.libvirt.org/page/Main_Page>`_.

Problem was though that the networking was virtual, and didn't pull an IP address from my router, so it wasn't public. There were a few sections here and there describing how to switch to bridged, and I tried them. They didn't work for me, either I suck at following directions, or they just won't work how I expect them to. You can see for yourself `here <http://wiki.libvirt.org/page/Networking#Fedora.2FRHEL_Bridging>`_ at how I attempted network bridging.

What I did was much more in my realm of knowledge, is simpler than all the other options, and is something I can make changes to w/o killing my network connectivity. iptables! I just used NAT forwarding. It was 2 lines, put in my pre-existing firewall script. So to get my local box 192.168.1.199 on port 2022 to forward to its internal virtual network of 192.168.100.2 at port 22 was as plain as this:


.. code-block:: bash

    $ iptables -t nat -I PREROUTING -p tcp --dport 2022 -j DNAT\
        --to-destination 192.168.100.2:22
    $ iptables -I FORWARD -p tcp --dport 22 -d 192.168.100.2 -j ACCEPT


One preroute rule to grab the port incoming, and one forward rule to pass said packets along. Now I have connectivity into my class virtual machine, and I don't have to do much to add more ports as needed. I am pretty happy with the setup so far. It's really nice to be able to connect remotely, vnc or ssh now, as well as know that I've limited the ram and cpu time the class can use on my box. I am interested to hear if anyone else is doing similar things with virtualization on their desktops.
