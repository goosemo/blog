---
title: Getting twitter feed running for Blogofile
date: 2010/09/28 19:21:05
Catagories: Programming, Website
tags: python, javascript, twitter, blogofile
---

A small part to making it match
-------------------------------

Wordpress_ has plugins, lots and lots of plugins. In my conversion from it to
blogofile_ I wanted to make it match my old site as closely as I could. Having
a twitter feed of my latest tweets was something I'd have to get on the site.

Fails
-----

I though I might make a python api call and then pipe that into my sidebar.
This worked. But it sucked because I'd have to rebuild the page every tweet. I
don't mind static content for my posts and navigation and the like. That's just
good caching I feel. 

Tweets though are a constantly, or would be for anyone else but me, updating
service. 

In comes the JavaScript
-----------------------

So in looking for simple things to give me a twitter feed I found Remy Sharp's
site and his directions_ on how to put a javascript based feed into a site.

It was simple as could be, and I had a base, but hard coded feed up an running
in short order.


Making it better for blogofile users
------------------------------------

Part of open source is giving back. Something I really want to do more of, and I
feel am getting into the swing of it a bit more. But that's whatever, I found
the useful and perfect plugin, and got it working in blogofile_ without much
trouble.

I now started thinking about how others might like to use this and would not
really want to hard code it too much. So I made it into a controller, and
configurable by the **_config.py** file. I made it kinda simple, but a bit
overkilled with the folder and an __init__.py, but I was aiming for it to be
more work. 

_controllers/tweets/__init__.py
===============================

.. code-block:: python

    import logging
    
    from blogofile.cache import bf
    
    config = {
        "name": "Twitter",
        "description": "Makes a sidebar widget for twitter",
        "priority": 70.0,
        }

    def run():
        tweets = bf.config.controllers.tweets
        tweets.logger = logging.getLogger(config['name'])


After making it a controller then we're able to put in config vars and set them
as we want. Which makes it nice for me later i want to change some things,
since all configs are in this one file.

_configure.py
=============

.. code-block:: python

    ### Twitter Settings ###
    controllers.tweets.enabled = True
    tweets = controllers.tweets
    tweets.username = "morganiangoose"
    tweets.count = 3
    tweets.enable_links = 'true'
    tweets.ignore_replies = 'false'
    tweets.template = ('<li><div class="item">%text% <a href="http://twitter.c'
            'om/%user_screen_name%/statuses/%id%/">%time%</a></div></li><br/>')


I then threw this, which is pretty much directly from remy's directions_ with
mako var, into my sidebar template. 

_templates/sidebar.mako
=======================

.. code-block:: html

    <div class="sidebar_item">
    <h3>Twitter</h3>
        <script src="http://twitterjs.googlecode.com/svn/trunk/src/twitter.min.js" 
        type="text/javascript"></script>
        <script type="text/javascript" charset="utf-8">
            getTwitters('tweet', { 
                id: '${bf.config.tweets.username}', 
                count: ${bf.config.tweets.count}, 
                enableLinks: ${bf.config.tweets.enable_links}, 
                ignoreReplies: ${bf.config.tweets.ignore_replies}, 
                clearContents: true,
                template: '${bf.config.tweets.template}',
                });
        </script>
        <div id="tweet">
        </div>
    </div>
    <br />
    
Now when I compile the site it'll just throw all this into the sidebar, which
will load up my twitter feed as I described in the template. And I won't have
to have a twitter trigger or the like for updating my blog, which is I feel the
best of both worlds. 

.. _blogofile: http://www.blogofile.com
.. _directions: http://remysharp.com/2007/05/18/add-twitter-to-your-blog-step-by-step/
.. _Wordpress: http://wordpress.org
