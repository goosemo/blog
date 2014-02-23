import logging

from blogofile.cache import bf
github = bf.config.controllers.github

from github3 import gh as github_api

config = {
    "name": "Github",
    "description": "Makes a nice github project listing for the sidebar",
    "priority": 95.0,
    }

def get_list(user):
    """
    Each item in the list has:
        name, url, description, forks, watchers, homepage, open_issues

    """
    return [g for g in github_api.iter_user_repos(user) if not g.fork]


def run():
    github.logger = logging.getLogger(config['name'])
    github.repo_list = get_list(github.user)
    github.full_repo_list = github_api.iter_user_repos(github.user)
