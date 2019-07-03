from geopy.geocoders import Nominatim

# Create A GeoLocator Object
geolocator = Nominatim(user_agent="HyeRyeong_Song_app")

# To geolocate a query to an address
location = geolocator.geocode("175 5th Avenue NYC", addressdetails=True)

print(location.address)

print((location.latitude, location.longitude))

print(location.raw)

# To find the address corresponding to a set of coordinates
location = geolocator.reverse("52.509669, 13.376294", addressdetails=True)

print(location.address)

print(location.raw)

# print specific part of the address

print(location.raw['address']['city'])