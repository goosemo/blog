from fabric.api import *


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
    local("scp -r _site/{blog,css} %s:/var/www/html/" % env.host_string)


