import httplib2
import json

def getGeocodeLocation(location):
    google_api_key = "AIzaSyAdOGJlu6X6AKFCeclpI0d_J6mwS93UIvI"
    locationString = location.replace(" ", "+")
    # creating a url with the location string and api key
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' %(locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    # getting the longitude and latitude out of the json
    longitude = result['results'][0]['geometry']['location']['lng']
    latitude = result['results'][0]['geometry']['location']['lat']
    return longitude, latitude
