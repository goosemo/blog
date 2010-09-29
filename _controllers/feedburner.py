import logging

from blogofile.cache import bf

config = {
    "name": "Feedburner",
    "description": "Makes the comments RSS point to feedburner",
    "priority": 70.0,
    }

def run():
    feedburner = bf.config.controllers.feedburner
    feedburner.logger = logging.getLogger(config['name'])


