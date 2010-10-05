import logging
import adsense
import analytics
import feedburner

from blogofile.cache import bf
google = bf.config.controllers.google

config = {
    "name": "Google",
    "description": "The controler for all the google tools I use",
    "priority": 95.0,
    }


def run():
    google.logger = logging.getLogger(config['name'])
    adsense.run()
    analytics.run()
    feedburner.run()

