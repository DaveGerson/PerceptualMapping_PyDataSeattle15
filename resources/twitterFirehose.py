#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'gerson64'
from twython import TwythonStreamer
import sys

class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
            sys.stdout.flush()



    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

restList = ["@Textastrophe", "@YouTube", "@iPhoneTeam", "@KatyPerry", "@TheEllenShow", "@HuffingtonPost",
            "@TweetsofOld", "@BarackObama", "@cnnbrk"]

track = ' , '.join(restList)


twitter_token = "EtQF2YGPr448k1eXGbUAKdOaa"
twitter_secret = "xaGuEs3b8Socsp8lB6xBCBP6P1WnQLsklqXRqngfK32NWKMibc"
access_token = "270963696-vt4BlPvIpwi4XmuXJFXSRJctbxwSIPT0jxLBLTMB"
access_secret = "i9IgkLPGyX5jOS6bAk8wIjbBUJg54qvqUwuSktzMFTjzd"

streamer = TweetStreamer(twitter_token, twitter_secret,
                         access_token, access_secret)

streamer.statuses.filter(track = track)

