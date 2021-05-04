from termux import *
import requests as req 

api_key="pk.d4323833cd9c941006bffd8553c7a821"

location=get_location()
lat=str(location["latitude"])
lng=str(location["longitude"])

response=req.get("https://us1.locationiq.com/v1/reverse.php?key={}&lat={}&lon={}&format=json".format(api_key,lat,lng))

print("Gotcha!! You are at {}".format(str(response.json()["display_name"])))