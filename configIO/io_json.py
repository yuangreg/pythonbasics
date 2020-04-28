import json

dict = {'scale': 1, 'x0': 2, 'y0': 3}

# Saving Parameters
with open('params.json', 'w') as f:
    json.dump(dict, f)

# Loading Parameters
with open('params.json', 'r') as f:
    config = json.load(f)