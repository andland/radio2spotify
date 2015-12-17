# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 11:19:33 2014

@author: Andrew Landgraf
"""

from bs4 import BeautifulSoup
import requests
import re

def scrape_cd1025_songs(num = 50):
    url = "http://cd1025.com/about/playlists/now-playing"
    
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    # table = soup.find("table")
    
    artists = []
    titles = []
    counter = 1
    # for row in table.findAll('tr')[1:]:
    for row in soup.find_all('tr')[1:]:
        col = row.findAll('td')
        artist = col[1].text
        title = col[2].text
        artist = artist.replace("THE FOO FIGHTERS", "FOO FIGHTERS")
        artist = artist.replace("THE VIOLENT FEMMES", "VIOLENT FEMMES")
        title = title.replace("(BIG ROOM)", "")
        artists.append(artist.strip())
        titles.append(title.strip())
        
        if counter >= num:
            break
        else:
            counter = counter + 1
        # print artist + ' - ' + title
    
    artists.reverse()
    titles.reverse()
    return artists, titles

def scrape_wxrt_songs(num = 50):
    url = "http://wxrt.cbslocal.com/playlist/"
    
    r  = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    artists = []
    titles = []
    counter = 1
	# use selectorGadget to get CSS selector info
    for item in soup.select(".track-info"):
        title = item.select(".track-title")
        artist = item.select(".track-artist")
		# the info is between quotes
        artists.append(re.findall(r'\"(.+?)\"',str(artist))[1] )
        titles.append(re.findall(r'\"(.+?)\"',str(title))[1])
        
        if counter >= num:
            break
        else:
            counter = counter + 1
    
    #print artists[0] + " - " + titles[0]
    artists.reverse()
    titles.reverse()
    return artists, titles


#if __name__ == "__main__":
#    artists, titles = scrape_cd1025_songs()
#    spotify_search_base = "https://api.spotify.com/v1/search?q="
#    i=len(artists)-1
#    song_search = "artist:" + artists[i].replace(" ", "%20") + "%20track:" + titles[i].replace(" ", "%20")
#    url = spotify_search_base + song_search + "&type=track&limit=1"
#    print url
#    # r  = requests.get(url)
#    data = json.load(urllib2.urlopen(url))
#    print data
    
#def get_track_ids(artists, titles):
#songs = []
#for i in range(0, len(artists)):
#    song_search = "artist:" + artists[i].replace(" ", "%20") + "%20track:" + titles[i].replace(" ", "%20")
#    songs.append("artist:" + artists[i].replace(" ", "%20") + "%20track:" + titles[i].replace(" ", "%20"))



# TODO: Get song id for each song
# TODO: Build playlist from songs
# TODO: Scrape WZRT

# https://developer.spotify.com/web-api/search-item/
# https://api.spotify.com/v1/search?q=THE%20WHITE%20STRIPES%20BLUE%20ORCHID&type=track&limit=1
# "id" : "1PCA097woCMSDvZPUVeRI7"
# https://developer.spotify.com/web-api/get-several-tracks/
