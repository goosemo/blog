# -*- coding: utf-8 -*-

######################################################################
# This is the main Blogofile configuration file.
# www.Blogofile.com
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site.url = "http://morgangoose.com"

#### Blog Settings ####
blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = "/blog"

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "Magoo"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "affiliated with the society of blog bloggables"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "US/Eastern"

## extra blog settings ##
blog.latest_post_count = 8
blog.posts_per_page = 2

### Twitter Settings ###
controllers.tweets.enabled = True
tweets = controllers.tweets
tweets.username = "morganiangoose"
tweets.count = 3
tweets.enable_links = 'true'
tweets.ignore_replies = 'false'
tweets.template = ('<li><div class="item">%text% <a href="http://twitter.c'
         'om/%user_screen_name%/statuses/%id%/">%time%</a></div></li><br/>')

######################################################################
# Intermediate Settings
######################################################################
#### Feedburner settings ####
controllers.feedburner.enabled = True
feedburner = controllers.feedburner
feedburner.url = "http://feeds.feedburner.com/morgangoose/FCyR"

#### Google Analytics ####
controllers.google_analytics.enabled = True
google_analytics = controllers.google_analytics
google_analytics.id = "UA-9907711-1"

#### Disqus.com comment integration ####
blog.disqus.enabled = True
blog.disqus.name    = "magoo"

### Syntax highlighter ###
# You can change the style to any builtin Pygments style
# or, make your own: http://pygments.org/docs/styles
filters.syntax_highlight.style   = "fruity"
filters.syntax_highlight.css_dir = "/css"
filters.syntax_highlight.preload_styles = ["murphy","monokai","fruity"]
#### Custom blog index ####
# If you want to create your own index page at your blog root
# turn this on. Otherwise blogofile assumes you want the
# first X posts displayed instead
blog.custom_index = False

#Post excerpts
#If you want to generate excerpts of your posts in addition to the
#full post content turn this feature on
post_excerpt_enabled     = True
post_excerpt_word_length = 25
#Also, if you don't like the way the post excerpt is generated
#You can define a new function
#below called post_excerpt(content, num_words)


######################################################################
# Advanced Settings
######################################################################

#### Default post filters ####
# If a post does not specify a filter chain, use the 
# following defaults based on the post file extension:
blog.post_default_filters = {
    "markdown": "syntax_highlight, markdown, paragraph_permalinks",
    "textile": "syntax_highlight, textile, paragraph_permalinks",
    "org": "syntax_highlight, org, paragraph_permalinks",
    "rst": "syntax_highlight, rst, paragraph_permalinks",
    "html": "syntax_highlight, paragraph_permalinks"
}

### Pre/Post build hooks:
def pre_build():
    #Do whatever you want before the _site is built
    pass

def post_build():
    #Do whatever you want after the _site is built
    pass




