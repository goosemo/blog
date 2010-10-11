import logging

from blogofile.cache import bf
reddit = bf.config.controllers.reddit

config = {
    "name": "Reddit",
    "description": "Reddit stuff",
    "priority": 95.0,
    }


def run():
    reddit.logger = logging.getLogger(config['name'])
