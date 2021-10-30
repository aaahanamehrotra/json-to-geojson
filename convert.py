import json

f = open('output.json')
data = json.load(f)
# x = []
 
# for i in data:
#     dict_a = {
#         "latitude": i["latitude"],
#         "longitude": i["longitude"]
#     }
#     x.append(dict_a)

# with open('new.json', 'w') as json_file:
#   json.dump(x, json_file)

from geojson import Point, Feature, FeatureCollection, dump
features = []
for i in data[1:]:
    print(i["latitude"], i["longitude"])
    point = Point((float(i["longitude"]), float(i["latitude"])))
    features.append(Feature(geometry=point, properties={"test": "test"}))

feature_collection = FeatureCollection(features)

with open('myfile.geojson', 'w') as file:
   dump(feature_collection, file)