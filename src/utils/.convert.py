import json
import os

# The top argument for walk
topdir = '.'
 
# The extension to search for
exten = '.json'
data = []
for dirpath, dirnames, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            if 'site' not in dirpath and 'github' not in dirpath:
                data.append(os.path.join(dirpath, name))

for json_file in data:
    print(json_file)
    with open(json_file) as json_file:  
        json_data = json.load(json_file)
        print(json_data)
