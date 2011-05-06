import logging
from . import adsense, feedburner

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
    if google.analytics.enabled:
        from . import analytics
        analytics.run()
    feedburner.run()

