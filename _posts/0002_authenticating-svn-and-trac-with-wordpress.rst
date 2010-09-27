---
categories: Webservers
date: 2009/05/07 14:05:16
guid: http://morgangoose.com/blog/?p=15
permalink: http://morgangoose.com/blog/2009/05/authenticating-svn-and-trac-with-wordpress/
tags: server, apache, mysql, wordpress, svn, trac
title: Authenticating svn and trac with wordpress
---
**Problem caused by wordpress upgrade**

My club uses Wordpress and I have our forums and subversion authenticate via the wordpress install's user table. This became very useful, and something that I tried to make sure I could apply on any new app I would install for the site. 

When trying to get the same thing setup for an install of Trac I had just made I ran into a bit of trouble.  With the old versions of wordpress this was pretty simple to do. Just a few lines in an apache conf file and we were golden.

With the most recent revisions though their implementation of password storage changed, causing the old setup to break for svn, and causing me a nice headache when trying to duplicate my old fix for svn onto trac.  They went from a simple md5 hash to using a much more secure phpass. (why it isn't phppass I don't know)

The main problem with this is that this isn't an authentication encryption that apache's mysql handler could use.  I tried to find a work around to get back to md5, but I couldn't find any. It was probably for the best anyhow, as I'd rather the site be more secure, than have more tools. No point in propagating something that could be exploited. Searching around some more I found the awesome work of Nikolay_. given out on Barry_'s blog, and explaining the install process.  Nikolay_ made an apache module to compile that added in the ability to use phpass. This compiled great and worked with the fedora install the server is on,  so the old fix for subversion was working again, with a single line changed.

**Subversion:**

.. code-block:: apache

    RedirectMatch ^(/repos)$ $1/
    <Location /repos/>
         Options all
         DAV svn
         SVNParentPath /repos/gcc/
         SVNListParentPath on
    
         AuthName "MySQL authentication for SVN"
         AuthType Basic
         Require valid-user
    
         AuthMYSQLEnable on
         AuthBasicAuthoritative off
         AuthMySQLAuthoritative on
    
         AuthMySQLHost localhost
         AuthMySQLUser user
         AuthMySQLPassword password
         AuthMySQLDB wordpress_db
         AuthMySQLUserTable wp_users
         AuthMySQLNameField user_login
         AuthMySQLPasswordField user_pass
         AuthMySQLPwEncryption phpass
    </Location>
    CustomLog logs/svn_logfile "%t %u %{SVN-ACTION}e" env=SVN-ACTION

That is the config that makes sure that only people that have accounts on the wordpress blog can have access to the repos. I plan on soon adding in a SVN auth file to make the commit users  more constrained, but at the moment, it isn't a priority.

The last line makes nice entries of SVN access in its own log file, which is very handy for debugging problems.

**Trac**

For trac I took the simple apache auth they provided on their website, and applied the same idea from svn to it:

.. code-block:: apache

    <Location "/projects/project-name/login">
         AuthType Basic
         Require valid-user
    
         AuthName "Trac Auth"
         AuthMYSQLEnable on
         AuthMySQLAuthoritative on
         AuthMySQLHost localhost
         AuthMySQLUser wordpress
         AuthMySQLPassword password
         AuthMySQLDB wordpress_db
         AuthMySQLUserTable wp_users
         AuthMySQLNameField user_login
         AuthMySQLPasswordField user_pass
         AuthMySQLPwEncryption phpass
    </Location>

I plan to use this type of database integration more, specifically with a wiki installation. Although I don't know of any wiki that could use this type of authentication as I am only familiar with mediawiki, and really only as a user.

.. _Barry: http://barry.wordpress.com/2008/05/19/mod_auth_mysql-and-phpass/
.. _Nikolay: http://nikolay.bg/

