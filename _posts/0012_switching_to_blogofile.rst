---
categories: python, website
tags: python, static, web, programming
title: Switching to Blogofile
date: 2010/09/28 13:03:00
---

So wordpress is out
-------------------

It had a nice run, and really did a lot of things I liked, highest among those
being that it worked. But even with my vim plugin for posting to the site, I
never really found myself happy with the whole setup. Then I stumbled upon
blogofile_ via a fork I spied in my github feed. After inspecting the project
and reading though the docs a bit I decided to give it a try.

.. _blogofile: http://www.blogofile.com

Conversion process
------------------

It was criminal how simple this was. I added Disqus_ comments (should have done
that ages ago) and imported all my old comments to the account. After that I
followed the directions_ to switch from wordpress and used the two scripts they
provided. After a few mysql hickups (dumped the db to a machine that had
python-mysql), the scripts worked flawlessly.

.. _Disqus: http://disqus.com/
.. _directions: http://www.blogofile.com/documentation/migrating_blogs.html#wordpress

I now had all of my posts, not a lot granted, in html blogofile_ form. Now I
mainly switched so that I could write up my posts in rst_ which I like a lot,
and use in other projects_. So now I had some conversions to make by hand to
get these posts into rst form.

.. _rst: http://docutils.sourceforge.net/rst.html
.. _projects: http://morgangoose.com/blog/2010/02/gnu-tools-presentation/

After some hand editing
-----------------------

I go to publish the site, and it's not liking my code-block directives. I use
these in other presentations and forgot that I'd made some changes to use the
directive, which I go into more depth about in a previous post_, but needed to
now retrofit into this project.

.. _post: 

The simple blog template had some helpers, but I had to pull the
rst_template.py filter from the blogofile.com template and edit it to give me the
highlighting control that I wanted. 

:rst_template.py changes:

.. code-block:: python

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
    from docutils.core import publish_parts, default_description
    
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

            print >>open('css/pygments_fruity.css', 'w'), formatter.get_style_defs(
                    '.highlight')
            parsed = highlight(u'\n'.join(self.content), lexer, formatter)
            return [nodes.raw('', parsed, format='html')]
    

    config = {
        'name' : "reStructuredText",
        'description' : "Renders reStructuredText formatted text to HTML",
        'aliases' : ['rst']
    }

    def run(content):
        directives.register_directive('sourcecode', Pygments)
        directives.register_directive('code-block', Pygments)
        directives.register_directive('code', Pygments)

        description = ('Generates S5 (X)HTML slideshow documents from standalone '
                'reStructuredText sources.  ' + default_description)

        return publish_parts(content, writer_name='html')['html_body']

So I added a lot into my site, and put in the theme I wanted to use in the css/
folder so that the style would publish when I build the site.
