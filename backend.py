# -*- coding: utf-8 -*-
"""
Created on Fri Aug 08 17:17:33 2014

@author: Andrew Landgraf
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
    <html>
    <head>
    <title>Radio2Spotify</title>
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
    </head>
    
    <body>
    <div>
    <h2 id='title'> Radio2Spotify </h2>
    Station: <select onchange="changeStation()" id="selectOpt">
  <option value="CD1025">CD1025</option>
  <option value="WXRT">WXRT</option>
</select>
<br>
<iframe src="%s" width="300" height="380" frameborder="0" allowtransparency="true" id="playlist"></iframe>
</div>

 
 <div class ='description'>
        This app scrapes the latest songs played on your favorite radio station
        and creates a Spotify playlist from them. This is meant for radio stations
        that do not have online streaming available. The code for this app can 
        be found on <a href="https://github.com/andland/radio2spotify">Github</a>.
</div>
</body>
 </html>
 """%playlist_url

if __name__ == '__main__':
    app.debug = True
    app.run()