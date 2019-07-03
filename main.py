from geopy.geocoders import Nominatim

# Create A GeoLocator Object
geolocator = Nominatim(user_agent="HyeRyeong_Song_app")

# To geolocate a query to an address
location = geolocator.geocode("175 5th Avenue NYC", addressdetails=True)

print(location.address)

print((location.latitude, location.longitude))

print(location.raw)