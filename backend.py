# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 17:17:33 2014

@author: Andrew
"""

from flask import Flask
from create_playlist import create_playlist

app=Flask(__name__)

@app.route('/<station>')
def get_station_playlist(station):
    return create_playlist(station)

@app.route('/')
def index():
    playlist_url = create_playlist("CD1025")
     
    return """
    <script>
    function changeStation(){
    xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
      {
          if (xmlhttp.readyState == 4) {
              document.getElementById("playlist").src=xmlhttp.responseText;
          }

      }
    var myselect = document.getElementById("selectOpt");
    var station = myselect.options[myselect.selectedIndex].value;
    
    xmlhttp.open("GET", station, true);
    xmlhttp.send();
  }
  
    </script>
    <div>
    <select onchange="changeStation()" id="selectOpt">
  <option value="CD1025">CD1025</option>
  <option value="WXRT">WXRT</option>
</select></div>
 <iframe src="%s" id="playlist">
 
 
 """%playlist_url

if __name__ == '__main__':
    app.debug = True
    app.run()