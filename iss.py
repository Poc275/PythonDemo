# demos virtual envs, 3rd party libs, http requests, json -> dicts

# Highly recommend using a new Python virtual environment when starting a new project 
# to keep all of your packages nicely isolated. This keeps you "global" Python environment 
# clean and helps prevent any package versioning conflicts down the line.
# To create follow this tutorial: https://docs.python.org/3/tutorial/venv.html
# To create a requirements.txt file to share with other devs: pip freeze > requirements.txt
# (remember to do this from your virtual environment)

# `pip install requests` to install it from PyPi
import requests

# calling the Open Notify API which is an open source project for 
# exposing some of NASA's data via an API
# get the current position of the ISS
iss_req = requests.get("http://api.open-notify.org/iss-now.json")
iss_json = iss_req.json()

print(iss_json)

iss_lat = iss_json["iss_position"]["latitude"]
iss_lon = iss_json["iss_position"]["longitude"]

print(iss_lat, iss_lon)

# convert lat/lon to a place using the geocode.xyz API
# might not work as it is a free API and heavily throttled
params = {
    "locate": "{0},{1}".format(iss_lat, iss_lon),
    "json": 1
}
geocode_req = requests.get("http://geocode.xyz", params=params)
geocode_json = geocode_req.json()

# print(geocode_json)

if geocode_json["matches"] is None:
    print("The ISS is somewhere near: ", geocode_json["suggestion"])

else:
    print("The ISS is over: ")
    if geocode_json.get("prov"):
        prov = geocode_json["prov"]
        print("Country code:", prov, "\n")

    if geocode_json.get("country"):
        country = geocode_json["country"]
        print("Country:", country, "\n")

    if geocode_json.get("region"):
        region = geocode_json["region"]
        print("Region:", region, "\n")

    if geocode_json.get("city"):
        city = geocode_json["city"]
        print("City:", city)
