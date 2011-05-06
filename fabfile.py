import os 

from fabric.api import *

def package():
    """
    Take the hardcoded list of files, and make tarball
    """
    with lcd("_site/"):
        local(("tar zcvf ../blog.tgz blog css projects p images about "
            "posts js docs sitemap.xml blank.html "))

def new_post(post_name):
    """
    Touch a dummy post, and make default header

    Be sure to feed in the name with spaces and use format of:
        fab new_post:"new post title"

    """
    post_template = "\n".join([
        "---",
        "title: %(post_name)s",
        "date: %(post_date)s",
        "draft: true",
        "---"])

    post_date = "2000/01/01 00:00:01"
    post_format = "_posts/0000_%s.rst"
    post_filename = "_".join(post_name.split(" "))
    with open(post_format % post_filename, 'w') as post:
            post.write(post_template % locals())


def _get_next_post_number():
    """
    Helper function that from the 4 long start number will find next.
    """
    return "%04d" % (max([int(x[:4]) for x in os.listdir('_posts')]) + 1)


def drafts():
    """
    Will list out posts that are still drafts
    """
    for post in [x for x in os.listdir('_posts') if x.startswith("0000")]:
        print post

def publish(post_name):
    """
    Take the draft post made by new_post() and make live

    Will find the time now, change that in the post, then also move the post to
    a new post name with the next number in the _posts dir's listing of
    existing post numbers.

    """
    from datetime import datetime

    now = datetime.now()
    old_post_date = "2000/01/01 00:00:01"
    post_date = now.strftime('%Y/%m/%d %H:%M:%S')
    post_format = "_posts/0000_%s.rst"
    post = post_format % "_".join(post_name.split(" "))
    local("sed -i -e's!%s!%s!' %s" % (old_post_date, post_date, post))
    local("mv _posts/0000%(name)s.rst _post/%(post)s_%(name)s.rst" % {
        'post':_get_next_post_number(),
        'name':"_".join(post_name.split(" "))})

def install():
    """
    Install deps using pip
    """
    local("sudo pip install -r requirements.txt")

def test_local():
    """
    Build blog, and run locally on port 9000
    """
    local("blogofile build")
    local("blogofile serve 9000")

@hosts('h4941w83@morgangoose.com')
def test():
    """
    Build, make sitemap, package, deploy.
    """
    local("export WORKON_HOME=$HOME/.virtualenvs; source /usr/bin/virtualenvwrapper.sh; workon blog; blogofile build")
    local(("python _extensions/sitemap_gen/sitemap_gen.py "
        "--config=_extensions/sitemap_gen/config.xml"))

    package()
    put("blog.tgz", "var/www/html/test/")
    local("rm blog.tgz")
    with cd("var/www/html/test/"):
        run("tar zxvf blog.tgz")

@hosts('h4941w83@morgangoose.com')
def build():
    """
    Build, make sitemap, package, deploy.
    """
    local("export WORKON_HOME=$HOME/.virtualenvs; source /usr/bin/virtualenvwrapper.sh; workon blog; blogofile build")
    local(("python _extensions/sitemap_gen/sitemap_gen.py "
        "--config=_extensions/sitemap_gen/config.xml"))

    package()
    put("blog.tgz", "var/www/html/")
    local("rm blog.tgz")
    with cd("var/www/html/"):
        run("tar zxvf blog.tgz")


