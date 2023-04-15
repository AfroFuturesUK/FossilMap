import requests
import folium
import geopy
import os
import webbrowser

# Make a request to the API to get the data
response = requests.get('https://www.nhm.ac.uk/api/dino-directory-api/dinosaurs')
data = response.json()

# Create a map
map = folium.Map(location=[0, 0], zoom_start=2)
geolocator = geopy.Nominatim(user_agent="my-app")

# Add natural history museum to map
folium.Marker(location=[51.4966, -0.1764], popup="Natural History Museum", icon=folium.Icon(color='red')).add_to(map)

global_south = ['Africa', 'Asia', 'South America']

# Loop through the data and add markers for each dinosaur found in the Global South
for dino in data:
    for country in dino.get('countries'):
        if country.get('continent').get('continent') in global_south:
            genus = dino.get('genus')
            print(str(genus) + ": " + str(country.get('country')))
            location = geolocator.geocode(country.get('country') + ", " + country.get('continent').get('continent'))
            if location:
                latitude = location.latitude
                longitude = location.longitude
                marker = folium.Marker(location=[latitude, longitude], tooltip=genus)
                marker.add_to(map)

# Display the map
map.save("AfricanDinos.html")

# Open the HTML file in a web browser
webbrowser.open("file://" + os.path.realpath("AfricanDinos.html"))