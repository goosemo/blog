# Set to True if you want inline CSS styles instead of classes
INLINESTYLES = False
STYLE = "fruity"

from pygments.formatters import HtmlFormatter

# The default formatter
DEFAULT = HtmlFormatter(noclasses=INLINESTYLES, style=STYLE)

# Add name -> formatter pairs for every variant you want to use
VARIANTS = {
            # 'linenos': HtmlFormatter(noclasses=INLINESTYLES, linenos=True),
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
