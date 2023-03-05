import geocoder

place = '清水寺'
ret = geocoder.osm(place, timeout=5.0)
print(place, ret.latlng)