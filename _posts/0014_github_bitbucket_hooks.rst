---
title: Github and Bitbucket hooks
date: 2010/09/29 17:40:10
categories: Version Control
tags: hg, git, hooks, bash
---

I use hg but like github
------------------------

I also dislike unevenness. Having recently read about the hg-git_ plugin and 
read about a setup_ that uses the paths definitions for hg_ to make simple 
names to push to, and decided to combine them all together. I ended up with a
~/.hgrc that I had this:

.. _hg-git: http://hg-git.github.com/
.. _setup: http://hgtip.com/tips/advanced/2009-11-09-create-a-git-mirror/
.. _hg: http://hgbook.red-bean.com/index.html

.. code-block:: ini

    [extensions]
    hgext.bookmarks =
    hggit =


And then in the repo's .hg/hgrc I'd add something like this:

.. code-block:: ini

    [paths]
    github = git+ssh://git@github.com:goosemo/hooks.git
    bitbucket = ssh://hg@bitbucket.org/morgan_goose/hooks

That worked well
----------------

But I had to remember to push to both, and that was annoying. Then I dug into 
hooks_ and found that I could easily make a shell script to push to both for 
me. What I ended up with was a bash script that would determine which path I 
had pushes to, and then push to the other:

.. _hooks: http://www.selenic.com/mercurial/hgrc.5.html#hooks

.. code-block:: bash

    #!/bin/bash

    # This script takes in the args that a hg push is given and checks for the paths
    # that I've defined in my hg repos for either a push to bitbucket or github,
    # and then does the other, so that regardless of which of these sites I push to
    # the other also get pushed to.

    #post-push to bitbucket
    if [[ $HG_ARGS =~ "push bitbucket" ]]
    then 
        hg push github --quite
    fi

    #post-push to github
    if [[ $HG_ARGS =~ "push github" ]]
    then 
        hg push bitbucket --quite
    fi

Note that the quiet flags or similar must be employed, otherwise you'll get
caught in an infinite loop. After that I added this line into my ~/.hgrc

.. code:: ini

    [hooks]
    post-push = $HOME/workspace/hooks/github.sh


Success
-------

Now regardless of where I push the other will get the update:

.. code:: bash

    ~/workspace/hooks$ hg push bitbucket
    pushing to ssh://hg@bitbucket.org/morgan_goose/hooks
    searching for changes
    no changes found
    

    ~/workspace/hooks$ hg push github
    pushing to git+ssh://git@github.com:goosemo/hooks.git
    importing Hg objects into Git
    creating and sending data
    github::refs/heads/master => GIT:b4fb4c58

