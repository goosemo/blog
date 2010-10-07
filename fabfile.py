from fabric.api import *

def package():
    with cd("_site/"):
        local(("tar zcvf ../blog.tgz blog css projects p images about "
            "sitemap.xml "))

def new_post(post_name):
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


def publish(post_name):
    """
    sed -e's/draft: true/draft: false'
    """
    from datetime import datetime

    now = datetime.now()
    post_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print post_date
        

def install():
    local("sudo pip install -r requirements.txt")

def test():
    local("blogofile build")
    local("blogofile serve 9000")

@hosts('h4941w83@morgangoose.com')
def build():
    local("blogofile build")
    local(("python _extensions/sitemap_gen/sitemap_gen.py "
        "--config=_extensions/sitemap_gen/config.xml"))

    package()
    put("blog.tgz", "var/www/html/")
    with cd("var/www/html/"):
        run("tar zxvf blog.tgz")


