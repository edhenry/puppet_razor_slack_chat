__author__ = 'edhenry'

import httplib
import json
import requests
import sys


#Defined the class to use when submitting a post to a slack instance
class post_to_slack():
    def __init__(self, channel, username, icon, message, url):

        self.channel = channel
        self.username = username
        self.icon = icon
        self.message = message
        self.url = url
        self.slack_call()

    #Defines the object to use when posting to a slack integration
    def slack_call(self):
        payload = {'channel': self.channel,
                    'username': self.username,
                    'icon_emoji': self.icon,
                    'text': self.message
                    }

        return requests.post(self.url, json.dumps(payload))
