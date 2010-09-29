---
title: Github and Bitbucket hooks
date: 2010/09/29 17:40:10
---

I'd recently read about the hg-git_ plugin and read a site that uses the paths_
plugin for hg_ to make simple names to push to, and decided to combine them all
together. I ended up with a ~/.hgrc that I has these:

.. code-block:: ini

    [extensions]
    hggit=
    hgext.bookmarks =
    hgext.schemes=
    
    [schemes]
    github = git+ssh://git@github.com:goosemo
    bitbucket = ssh://hg@bitbucket.org/morgan_goose


And then in the repo's .hg/hgrc I'd add something like this:

.. code-block:: ini

    [paths]
    github = git+ssh://git@github.com:goosemo/hooks.git
    bitbucket = ssh://hg@bitbucket.org/morgan_goose/hooks

That worked well, but then I had to remember to push to both, and that was
annoying. Then I dug into hooks_ and found that I could easily make a shell
script to push to both for me. What I ended up with was a bash script that
would determine which path I had pushes to, and then push to the other:

.. code-block:: bash

    #!/bin/bash

    # This script takes in the args that a hg push is given and checks fo the paths
    # that I've defined in my hg repos for either a push to bitbucket or github,
    # and then does the other, so that regardless of which of these sites I push to
    # the other also get pushed to.

    #post-push to bitbucket
    if [[ $HG_ARGS =~ "push bitbucket" ]]
    then 
        hg push github
    fi

    #post-push to github
    if [[ $HG_ARGS =~ "push github" ]]
    then 
        hg push bitbucket
    fi

Then I added this line into my ~/.hgrc

.. code:: ini

    [hooks]
    post-push = $HOME/workspace/hooks/github.sh

