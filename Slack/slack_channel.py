__author__ = 'edhenry'

import httplib
import json
import requests
import sys

class slack_api:

    def __init__(self, channel, username, icon, url):

        self.channel = channel
        self.username = username
        self.icon = icon
        self.url = url

    def post_to_slack(self, message):

        #Defines the payload to push out the slack channel
        payload = {'channel': self.channel,
                    'username': self.username,
                    'icon_emoji': self.icon,
                    'text': message
                    }

        return requests.post(self.url, json.dumps(payload))
