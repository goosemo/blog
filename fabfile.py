from fabric.api import *

def package():
    with cd("_site/"):
        local("tar zcvf ../blog.tgz blog css projects p images about")

def new_post(post_name):
    post_template = """
    ---
    title: %{post_name}
    date: %{post_date}
    draft: true
    ---
    """

def publish(post_name):
    """
    sed -e's/draft: true/draft: false'
    """
    pass

@hosts('h4941w83@morgangoose.com')
def build():
    local("blogofile build")
    package()
    put("blog.tgz", "var/www/html/")
    with cd("var/www/html/"):
        run("tar zxvf blog.tgz")


