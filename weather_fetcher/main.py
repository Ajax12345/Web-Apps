from bottle import route, run, template, static_file, request
import urllib
import re
from bs4 import BeautifulSoup as soup
def get_forcast(latitude, longitude):
    url = "http://forecast.weather.gov/MapClick.php?site=EWX&lat={}&lon={}#.WbBrg4qQxLx".format(latitude, longitude)

    data = str(urllib.urlopen(url).read())
    
    final_data = soup(data, "lxml")
    table = final_data.findAll("div", class_="tombstone-container")
    new_text = [i.text for i in table]
    final_text = [i.split("\n") for i in new_text]
    new_table = """
     <table style="width:100%">
     <tr>
        <th>Time</th>
        <th>Conditions</th>
        <th>Temperature</th>
    </tr>
    """
    print final_text
    for c, a, b in final_text[1:]:
        print c, a, b
    formatted_data = '\n'.join("<tr>\n<td>{}</td>\n<td>{}</td>\n<td>{}</td>".format(a, b[:-5], b[-6:-3]) for c, a, b in final_text[1:])+"\n</table>"

    new_table += "\n"+formatted_data
    print formatted_data
    return new_table


    #print final_data
#@get("/")# or
@route('/')
def main_page():
    return open('/Users/davidpetullo/Documents/gpsfile/gps_corrdinates.html').read()


@route('/', method='POST')
def get_weather():
    lat = request.forms.get('latitude')
    l = request.forms.get('longitude')
    #get_forcast(lat, l)
    #return "<p> You entered {}lat {}long</p".format(lat, l)
    return get_forcast(lat, l)




run(host="127.0.0.1", port=8000, debug = True)
