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


twitter_token = ""
twitter_secret = ""
access_token = ""
access_secret = ""

streamer = TweetStreamer(twitter_token, twitter_secret,
                         access_token, access_secret)

streamer.statuses.filter(track = track)

