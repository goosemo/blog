import logging

from blogofile.cache import bf

config = {
        "name": "Twitter",
        "description": "Makes a sidebar widget for twitter",
        "priority": 70.0,
        "username": "morganiangoose",
        }

def run():
    tweets = bf.config.controllers.tweets
    tweets.logger = logging.getLogger(config['name'])

