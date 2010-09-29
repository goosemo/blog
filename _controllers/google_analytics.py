import logging

from blogofile.cache import bf

config = {
    "name": "Google Analytics",
    "description": "Makes the comments RSS point to google analytics",
    "priority": 70.0,
    }

def run():
    google_analytics = bf.config.controllers.google_analytics
    google_analytics.logger = logging.getLogger(config['name'])


