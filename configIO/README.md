# Parameters Saving and Loading

## Pickle
The mode has to be in binary 'b', i.e., 'wb' and 'rb'
````
# Saving Parameters
dict = {'scale': 1, 'x0': 2, 'y0': 3}
file = open('params', 'wb')
pickle.dump(dict, file)
file.close()

# Loading Parameters
file = open('params', 'rb')
dict = pickle.load(file)
````

## Json
````
dict = {'scale': 1, 'x0': 2, 'y0': 3}

# Saving Parameters
with open('params.json', 'w') as f:
    json.dump(dict, f)

# Loading Parameters
with open('params.json', 'r') as f:
    config = json.load(f)
````

## ElementTree

Use package
````
import xml.etree.ElementTree as ET
````

## ConfigParsor

Use package
````
from configparser import ConfigParser
````




