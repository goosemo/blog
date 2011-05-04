---
title: Authenticating Redmine from existing Wordpress users table
date: 2000/01/01 00:00:01
draft: true
---

Why would you want to
=====================

When I first setup the site for the `game creation club`_ at osu, it was
decided to use wordpress_ for the blogging software. We only needed a place to
put up content and have it world readable. This worked great, and when we later
needed a forum for the club, the makers of Wordpress_ already had bbPress_
going and it boasted a nice interegration with the existing user table.


Then came more
===============

A while back I wrote up a bit about how to `auth trac and svn`_ using a phpass
plugin for apache. Which allowed those two to use the same user tables simply
for all user auths. That also was nice since, people using the system had a
nice interface for updating passwords for these tools already, and knew how to
use it by then as well.


Now to add Redmine_
====================

Being that the club_ is one that has a number of programming projects at any
one time, a manager system with tickets would be an ideal addition. I'm also
now pretty familiar with Redmine_ because of the Fabric_ project, which uses it
at the moment. 

Redmine_'s install was simple enough, follwing directions got it up and running
pretty quickly. Did have to used thin to run it, as passenger wasn't liking me
running it in directory, that and I don't have subdomain rights for the club's
domain root (as that's osu.edu). 

Authentication
===============






# Compare input and stored hash
known = '$P$9IQRaTwmfeRo7ud9Fh4E2PdI0S3r.L0'
p phpass.check('test12345', known) # => true
p phpass.check('test12346', known) # => false




.. _auth trac and svn: http://morgangoose.com/blog/2009/05/authenticating-svn-and-trac-with-wordpress
.. _game creation club: http://gamdev.osu.edu
.. _club: http://gamdev.osu.edu
.. _phppass-ruby: https://github.com/uu59/phpass-ruby
.. _alternative custom authentication: http://www.redmine.org/projects/redmine/wiki/Alternativecustom_authentication_HowTo
.. _bug from ruby version change: http://www.redmine.org/issues/6196
.. _wordpress: http://wordpress.com
.. _Redmine: http://www.redmine.org/
