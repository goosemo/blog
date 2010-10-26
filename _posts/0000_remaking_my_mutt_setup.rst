---
author: Morgan Goose
title: Remaking my Mutt setup.
date: 2010/09/29 00:34:00
draft: true
categories: Programming
reddit: linux
---

Mutt is wonderful
-----------------

If you've not yet heard or of mutt_ or seen it in action, I would suggest going
out and looking it up now. It was the first in a line of many cli apps that I
now use daily. I can't really get used to another way to work with my mail
anymore. A brief reprieve due to moving places recently forced me to use gmail
only and it wan't anywhere near as simple.

.. _mutt: http://mutt.org

I could go into what mutt is and what it isn't, but there are many better posts
that do that out there. I'm just relaying my personal setup for aggregation,
spam catching, filtering into folders, and keeping everything in sync.


Original setup
--------------

Shortly after getting into mutt I made a, at the time, acceptable system for
getting my mail and sending out messages. I'd have the python script getmail_
grab my email via pop and imap and download them onto my machine. I'd also
setup a postfix_ server on my machine that forwarded out to my ISP's smtp
servers, so that sending email was a simple as possiable. I'd also setup a web
interface with roundcube to be able to check the setup when ssh wasn't reddily
avaliable.

.. _getmail:
.. _postfix: 

This worked well but had some holes. Sent mail wouldn't be anywhere but my
machine. Messages I deleted wouldn't delete on the server if I chose to leave
them there when I checked for new mail, so sometimes on limited accounts the
mailbox would fill up. The web interface relied on symlinks for the folder
names, which was a but tedious, and useless if I forgot to add a folder I
wanted. Spam wasn't filtered really, and while minor, would have been nice.

Leverage what is already in use
-------------------------------

I have about 4 email accounts, give or take a possiably expired school address.
One of which is a gmail account. Which recently (I think recently) allowed
access via IMAP, and I found will also do pop email downloading from other
email accounts.

So I can consolidate all my email into my gmail account. This gives me spam
protection, smart filters, and a web interface for free. Which are big, since
getting those on a server are a bit harder to setup, and the payoff is worth
less than the time cost, as well as being (to the best of my knowledge) subpar
with the ability of google to do these things.

Most of this is in the docs_ google provides, and is pretty simple to setup. It
also allows for a setup_ that gives google permission to send email as the email
accounts it imports from.

.. _docs:
.. _setup: 

How a program change made this nearly perfect
---------------------------------------------

I am a member of the `Open Source Club @ the Ohio State University
<opensource.osu.edu>`_ and there are a lot of smart people in that club, and a
lot of them also happen to be cli app lovers. Strangely only a few of us use
mutt_, but


Offlineimap
-----------

install from package manager & configure

.. code-block:: ini

    stuff


Test it pretty like
===================

blinken lights


Get this automated and in the background
========================================



Get mutt hopping along with these mailboxes
-------------------------------------------

lambda filter
=============


Side note to patch your Mutt_
=============================
