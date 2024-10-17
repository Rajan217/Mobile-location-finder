import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# Assuming 'number' is defined in the test module
number = "+918084547291"

# OpenCage API key
key = "a3b0c707fb594e428ec77bc8b61bfee7"

# Parsing the phone number
check_number = phonenumbers.parse(number)

# Getting the location information
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)

# Getting the service provider information
service_provider = carrier.name_for_number(check_number, "en")
print("Service Provider:", service_provider)

# Geocoding the location using OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(number_location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude:", lat, "Longitude:", lng)

# Creating a map using Folium
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("my location.html  ")
print("Map saved as 'my location.html '")