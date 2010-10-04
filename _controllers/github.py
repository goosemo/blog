import logging

from blogofile.cache import bf
github = bf.config.controllers.github

from github2.client import Github
github_api = Github()

config = {
    "name": "Github",
    "description": "Makes a nice github project listing for the sidebar",
    "priority": 90.0,
    }

def get_list(user):
    """
    Each item in the list has:
        name, url, description, forks, watchers, homepage, open_issues

    """
    return [g for g in github_api.repos.list(user) if not g.fork]


def run():
    github.logger = logging.getLogger(config['name'])
    github.repo_list = get_list(github.user)
    github.full_repo_list = github_api.repos.list(github.user)
