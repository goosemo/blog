---
title: Github project list
date: 2010/09/29 22:24:00
categories: Programming, Version Control, Website
tags: git, python, blogofile
---

Adding in more stuff
--------------------

It's mostly what I am working on atm for the blog. After using blogofile_ for a
few days now I've really gotten accustomed to writing up new things for it. It
is only python after all. So that helps. My newest idea was to have a listing of
my github projects in the sidebar.

.. _blogofile: http://blogofile.com

Seems simple enough
-------------------

Found a `good api in python <http://github.com/ask/python-github2>`_ for this. 
There was one that used javascript that would have also done the job, but I 
decided this could be slow and updated when the site was built, instead of 
needing to be updated real time.

After installing the github2_ module, I got right to it and started making a
controller for the widget. And I ended up with something like this:

.. _github2: http://github.com/ask/python-github2

github.py
=========

.. code-block:: python

    import logging

    from blogofile.cache import bf
    github = bf.config.controllers.github

    from github2.client import Github
    github_api = Github()

    config = {
        "name": "Github",
        "description": "Makes a nice github project listing for the sidebar",
        "priority": 90.0,
        }

    def get_list(user):
        """
        Each item in the list has:
        name, url, description, forks, watchers, homepage, open_issues
        """
        return [g for g in github_api.repos.list(user) if not g.fork]

    
    def run():
        github.logger = logging.getLogger(config['name'])
        github.repo_list = get_list(github.user)

With a configuration in _config.py like this:

.. code-block:: python

    #### github projects ####
    controllers.github.enabled = True
    github = controllers.github
    github.user = "goosemo"

And a simple github.mako file that I used mako's include_ function for:

.. _include: http://www.makotemplates.org/docs/syntax.html#syntax_tags_include

.. code-block:: html

    <div class="sidebar_item">
    <h3>Github Projects</h3>
    <ul>
    % for project in bf.config.controllers.github.repo_list:
        <li><a href="${project.url}" title="${project.name}">
        ${project.name}</a>&nbsp;${project.description}</li>
        <br/>
    % endfor
    </ul>
    </div>
    <br />

I did run into an issue
-----------------------

After getting this all down the site was acting strange. The frontage had the
listing of my git repos just as it was supposed to be. But I found that on
every other page the github section was blank. 

After tweaking and getting a bit frustrated, I read the blogofile_ code a bit
more for the controller sections, and got the idea to up the priority from 70
to 90. 

This did the trick, and I figure it was because the permalinks and other page
creation work was being done before the github.repo_list could be populated.


Thoughts so far
---------------

Overall the process from idea to working in blogofile_ is straightforward,
since it's nothing new in form of coding. Mako and python go well together.

Now I just need to get down a coherent way to publish these little bits I keep
adding, and to also make them completely configurable via the _config.py and 
isolated into their own units so that installation/use is a simple procedure.
