# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 21:08:10 2014

@author: Andrew Landgraf
"""

import json
import urllib2
import scrape_songs
#import webbrowser

def create_playlist(station, songs = 10):
    if station == "CD1025":
        artists, titles = scrape_songs.scrape_cd1025_songs(songs)
    elif station == "WXRT":
        artists, titles = scrape_songs.scrape_wxrt_songs(songs)
    
    if len(artists) != len(titles):
        raise Exception("Artists and titles don't match")
    
    spotify_search_base = "https://api.spotify.com/v1/search?q="
    #i=len(artists)-1
    #i=1
    ids = []
    for i in range(len(artists)):
        song_search = "artist:" + artists[i].replace(" ", "%20") + "%20track:" + titles[i].replace(" ", "%20")
        url = spotify_search_base + song_search + "&type=track&limit=1"
        data = json.load(urllib2.urlopen(url))
        try:
            ids.append(data['tracks']['items'][0]['id'])
        except IndexError:
            print "Could not find " + artists[i] + " - " + titles[i]
    
    playlist_base = "https://embed.spotify.com/?uri=spotify:trackset:" + station + ":"
    playlist_url = playlist_base + ",".join(ids)
    return playlist_url
    
#    webbrowser.open(playlist_url, new = 2)
#if __name__ == "__main__":
#    pl = create_playlist()
#    print pl