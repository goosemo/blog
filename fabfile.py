from fabric.api import *

def package():
    with cd("_site/"):
        local(("tar zcvf ../blog.tgz blog css projects p images about "
            "sitemap.xml "))

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

def install():
    local("sudo pip install -r requirements.txt")

def test():
    local("blogofile build")
    local("blogofile serve 9000")

@hosts('h4941w83@morgangoose.com')
def build():
    local("blogofile build")
    local("python _extenstions/sitemap_gen/sitemap_gen.py \
            --config=_extenstions/sitemap_gen/config.xml")

    package()
    put("blog.tgz", "var/www/html/")
    with cd("var/www/html/"):
        run("tar zxvf blog.tgz")


