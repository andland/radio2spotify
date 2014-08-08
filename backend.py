# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 17:17:33 2014

@author: Andrew
"""

from flask import Flask
from create_playlist import create_playlist

app=Flask(__name__)

@app.route('/')
def index():
    playlist_url = create_playlist()
    print playlist_url
    return """ <iframe src={} >""".format(playlist_url)

app.run()