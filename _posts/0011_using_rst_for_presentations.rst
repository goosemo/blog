---
title: Using rst for presentations
date: 2010/09/12 18:03:00
categories: Python, Programming
tags: rst, python
---

Presentations are hard
----------------------

Not even just giving them, but the process of taking an idea and putting it
down in a concise and clear manner, that will be simple to show and distribute.

I am not going to make a claim that I am good at giving or writing up
presentations, but I do think I have a pretty slick setup going for making them
simple to show and distribute with minimal effort.


reStructuredText
----------------

People may be familiar with it already, but it's a markup language that's well
supported in python and used in the Sphinx_ project. It fits my brain well (in
most places) and only requires a text editor. 

.. _Sphinx: http://sphinx.pocoo.org/

Since it comes with some tools to take a simple plain text document and
transform it into other well known formats (latex, html, and pdf), caused me
to use it in a number of projects and for notes without much friction.

How I use rst
-------------

I mentioned in a previous post_ about my setup and how I leverage fabric_ to
build and post my presentations, but I didn't really get too much into the
specifics of how the rst_ document was formatted, and built.

.. _post: http://morgangoose.com/blog/2010/02/how-fabric-gets-it-right/
.. _fabric: http://docs.fabfile.org
.. _rst: http://docutils.sourceforge.net/rst.html

I write a presentation in rst just like I would write any other document in
rst. The goal I had was to write once, and have that document change into other
formats without an issue. I do leverage a few classes and directives that
aren't in the normal rst toolbox, to get my presentations just so. But these 
aren't out of line, and after a tweak or two in my pipeline don't break the
other formats I build to.

s5
--

    S5 is a slide show format based entirely on XHTML, CSS, and JavaScript.

And rst2s5 takes a reStructuredText document and complies it into the
corresponding s5 representation. Giving back a plain html page with some
JavaScript magic that is simple to post and host.

No need for server side scripting, or fancy Apache/lighttpd/nginx setups or any
need for proxies or their kin. So using s5_ alone will give me the goal of
simple to show, since I can post a presentation and have accesses to it
anywhere there is internet and a browser. I can even keep a copy on a
thumb drive in case the internet dies, and browse the slides locally.

.. _s5: http://meyerweb.com/eric/tools/s5/


reST with s5
------------

To meet the last part of my goal, I have to have a simple distribution medium.
For a presentation that is a pdf. It's akin to a paper, even though it is much
more broken down and split up into slides. Leveraging the *handout* class that
the s5 and pdf converters from rst_ know, I am able to have parts of the
presentation invisible in slide form, and show up only when the presentation
is expanded, or complied into a pdf.

:eg:

.. code-block:: rst

    =========
    GNU tools
    =========
    ----------------------------
    *mostly for text processing*
    ----------------------------

    .. class:: right
    
        `Morgan Goose http://morgangoose.com`
        January 2010

    .. class:: handout
    
        This work is licensed under the Creative Commons 
        Attribution-Noncommercial-Share Alike 3.0 United States License. 
        To view a copy of this license, visit 
        http://creativecommons.org/licenses/by-nc-sa/3.0/us/ or send a letter
        to Creative Commons, 171 Second Street, Suite 300, San Francisco, 
        California, 94105, USA.


So the above will show my name on the first slide, but not the license. In the
pdf though that will all be on the first page. More tips on the s5 rst meshing
can be found on the docutils site's section for slide-shows_

.. _slide-shows: http://docutils.sourceforge.net/docs/user/slide-shows.html


Code blocks
-----------

Normal reST had code directives that will differentiate the code, and in most
instances (Sphinx/Trac) will attempt to highlight the code accordingly. I ran
into issues here because rst2pdf and rst2s5 had different ideas on what these
should be named and neither really was highlighting the code. After searching a
bit I found that pygments, a code highlighter in python, already had some
docutils hooks that they `mention on their site 
<http://pygments.org/docs/rstdirective/>`_.

Using that as a stepping stone I added in code, code-block, and source code,
directives to use pygments for the code they contained. In my presentations
though I made sure to only use code-block because this is the directive that
rst2pdf is expecting when it goes to format the document.

After that my code goes through the ringer as shown in the post_ I gave
for fabric, in the line executing the rst-directive.py file and passing in the
pygments css for the theme that I prefer.

the final rst-directive.py looks like this though:

.. code-block:: python

    # -*- coding: utf-8 -*-
    """ 
        The Pygments reStructuredText directive
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
        This fragment is a Docutils_ 0.5 directive that renders source code
        (to HTML only, currently) via Pygments.
    
        To use it, adjust the options below and copy the code into a module
        that you import on initialization.  The code then automatically
        registers a ``sourcecode`` directive that you can use instead of
        normal code blocks like this::
    
            .. sourcecode:: python
    
                My code goes here.
    
        If you want to have different code styles, e.g. one with line numbers
        and one without, add formatters with their names in the VARIANTS dict
        below.  You can invoke them instead of the DEFAULT one by using a
        directive option::
    
            .. sourcecode:: python
                :linenos:
    
                My code goes here.
    
        Look at the `directive documentation`_ to get all the gory details.
    
        .. _Docutils: http://docutils.sf.net/
        .. _directive documentation:
           http://docutils.sourceforge.net/docs/howto/rst-directives.html

        :copyright: Copyright 2006-2009 by the Pygments team, see AUTHORS.
        :license: BSD, see LICENSE for details.
    """
    
    # Options
    # ~~~~~~~
    
    # Set to True if you want inline CSS styles instead of classes
    INLINESTYLES = False
    STYLE = "fruity"
    
    from pygments.formatters import HtmlFormatter
    
    # The default formatter
    DEFAULT = HtmlFormatter(noclasses=INLINESTYLES, style=STYLE)

    # Add name -> formatter pairs for every variant you want to use
    VARIANTS = {
        'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=False),
    }


    from docutils import nodes
    from docutils.parsers.rst import directives, Directive
    
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name, TextLexer
    
    class Pygments(Directive):
        """ Source code execution.
        """
        required_arguments = 1
        optional_arguments = 0
        final_argument_whitespace = True
        option_spec = dict([(key, directives.flag) for key in VARIANTS])
        has_content = True
    
        def run(self):
            self.assert_has_content()
            try:
                lexer = get_lexer_by_name(self.arguments[0])
            except ValueError:
                # no lexer found - use the text one instead of an exception
                lexer = TextLexer()
            # take an arbitrary option if more than one is given
            formatter = self.options and VARIANTS[self.options.keys()[0]] or DEFAULT
    
            print >>open('pygments.css', 'w'), formatter.get_style_defs('.highlight')
            parsed = highlight(u'\n'.join(self.content), lexer, formatter)
            return [nodes.raw('', parsed, format='html')]

    directives.register_directive('sourcecode', Pygments)
    directives.register_directive('code-block', Pygments)
    directives.register_directive('code', Pygments)

    from docutils.core import publish_cmdline, default_description

    description = ('Generates S5 (X)HTML slideshow documents from standalone '
                   'reStructuredText sources.  ' + default_description)

    publish_cmdline(writer_name='s5', description=description)


