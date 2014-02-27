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
blog.name = "MorganGoose.com"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "notes about various technical subjects"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "US/Pacific"

## blog_permalinks ##

blog.auto_permalink.enabled
blog.auto_permalink.path = ":blog_path/:year/:month/:day/:title"


######################################################################
# Intermediate Settings
######################################################################

#### Disqus.com comment integration ####
blog.disqus.enabled = True
blog.disqus.name    = "magoo"

### Syntax highlighter ###
# You can change the style to any builtin Pygments style
# or, make your own: http://pygments.org/docs/styles
blog.filters.syntax_highlight.style   = "fruity"
blog.filters.syntax_highlight.css_dir = "/css"
blog.filters.syntax_highlight.preload_styles = ["fruity"]

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

######################################################################
# My additions
######################################################################

# Similar Posts
blog.similar_posts.enabled = False
blog.similar_posts.count = 3

# Tag cloud
#blog.tags.enabled = False #broken

# Controler Enables
controllers.tweets.enabled = True
controllers.google.enabled = True
controllers.github.enabled = True
controllers.reddit.enabled = True
controllers.stackoverflow.enabled = True

# Google supplied stuff 
# ----------------------
if controllers.google.enabled:
    google = controllers.google

    ## Feedburner settings
    feedburner = google.feedburner
    feedburner.enabled = True
    feedburner.url = "http://feeds.feedburner.com/morgangoose/FCyR"

    ## Adsense 
    adsense = google.adsense
    adsense.enabled = True

    ## Google Analytics
    google.analytics.enabled = True
    if google.analytics.enabled:
        analytics = google.analytics
        import password
        analytics.username = password.get_username()
        analytics.password = password.get_password()
        analytics.id = "UA-9907711-1"
        analytics.table_id = "ga:19940817"
        analytics.top_posts_number = 5
        analytics.app_name = "blogfile_top_posts"
        analytics.start_date = "2009-04-20"

        ### Top post count
        from datetime import date
        today = date.today()
        analytics.top_posts_enabled = True
        analytics.show_count = False
        analytics.end_date = today.strftime("%Y-%m-%d")


## github projects
if controllers.github.enabled:
    github = controllers.github
    github.user = "goosemo"
    github.link_watchers = True
    github.link_forks = True
    github.link_issues = True
    github.link_rss_feed = False

## stackoverflow config
if controllers.stackoverflow.enabled:
    stackoverflow = """ 
<a href="http://stackexchange.com/users/70175/morgan"><img src="http://stackexchange.com/users/flair/70175.png" width="208" height="58" alt="profile for Morgan on Stack Exchange, a network of free, community-driven Q&amp;A sites" title="profile for Morgan on Stack Exchange, a network of free, community-driven Q&amp;A sites" /></a>
"""

## Twitter Settings
if controllers.tweets.enabled:
    tweets = controllers.tweets
    tweets.username = "morganiangoose"
    tweets.count = 5
    tweets.enable_links = 'true'
    tweets.ignore_replies = 'false'
    tweets.template = ('<li class="item">%text% <a href="http://twitter.c'
            'om/%user_screen_name%/statuses/%id%/">%time%</a></li>')


## Reddit button
if controllers.reddit.enabled:
    reddit = controllers.reddit
    reddit.button = True


## menu
menu = {
        'home': '/blog',
        'about': '/about',
        'posts': '/posts',
        'projects': '/projects',
        'presentations': '/p',
    }

## links
links = (

        ('Fabric', 'SSH made awesome by wrapping in Python',
            'http://docs.fabfile.org'),

        ('GCC', 'Game creation club at OSU',
            'http://gamedev.osu.edu'),

        ('OSC', 'Open souce club at OSU',
            'http://opensource.osu.edu'),

        ('COPy', "Central Ohio's python group",
            'http://www.meetup.com/Central-Ohio-Python-Users-Group/'),

    )

## extra blog settings 
blog.latest_post_count = 8
blog.posts_per_page = 2


### Pre/Post build hooks:
def pre_build():
    #Do whatever you want before the _site is built
    pass

def post_build():
    #Do whatever you want after the _site is built
    pass




