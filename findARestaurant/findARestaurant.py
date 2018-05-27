import requests
from geocode import getGeocodeLocation
import json
import httplib2

url = 'https://api.foursquare.com/v2/venues/explore'
foursquare_client_id = "5EX5WDIQSCH5T0FF44WIBB35B1URTUCF0LKDVK5FBNJPJ5FO"
foursquare_client_secret = "KFPB0A0BS5OVVKKBZKCF35YD5OG3FYPQQ1O3MCMQPAGWKSVP"

def findARestaurant(location, mealType):
    location = input("Type the location!")
    mealType = input("Type the meal!")

    latitude, longitude = getGeocodeLocation(location)
    longlat = str(longitude) + ','+ str(latitude)

    params = dict(
      client_id=foursquare_client_id,
      client_secret=foursquare_client_secret,
      v='20180327',
      ll=longlat,
      query=mealType,
      limit=1
    )

    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    rest_data = data['response']['groups']
    restaurant = data['response']['groups'][0]['items'][0]['venue']
    if restaurant:
        restaurant_id = restaurant['id']
        restaurant_name = restaurant['name']
        unformatted_add = restaurant['location']['formattedAddress']
        restaurant_address = ""
        for item in unformatted_add:
            restaurant_address += item
            restaurant_address += " "

    # getting the picture url
    h = httplib2.Http()
    # building the url
    picture_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((restaurant_id,foursquare_client_id,foursquare_client_secret)))
    # request the picture data in a json format
    result = json.loads(h.request(picture_url, 'GET')[1])
    photo_data = result['response']['photos']['items'][0]
    # if there is a photo
    if photo_data:
        prefix = photo_data['prefix']
        suffix = photo_data['suffix']
        photo_url = prefix + '300x300' + suffix
    # if there is no photo
    else:
        photo_url = "https://cdn.pixabay.com/photo/2016/11/18/14/05/brick-wall-1834784_1280.jpg"
    restaurant_info = {'name': restaurant_name, 'address': restaurant_address, 'picture': photo_url}
    print(restaurant_info)

findARestaurant('Budapest', 'coffee')
