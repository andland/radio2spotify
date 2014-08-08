# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 20:36:11 2014

@author: Andrew
"""

from bs4 import BeautifulSoup
import requests
import re
#import json
#import urllib2
#import pandas as pd

def scrape_wxrt_songs():
    url = "http://wxrt.cbslocal.com/playlist/"
    
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    
    artists = []
    titles = []
    for item in soup.select(".playlist_item_track_info"):
        title = item.select(".track_title")
        artist = item.select(".track_artist")
        artists.append(re.findall(r'\"(.+?)\"',str(artist))[1] )
        titles.append(re.findall(r'\"(.+?)\"',str(title))[1])
    
    #print artists[0] + " - " + titles[0]
    artists.reverse()
    titles.reverse()
    return artists, titles

