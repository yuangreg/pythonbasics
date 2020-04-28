from configparser import ConfigParser

dict = {'scale': 1, 'x0': 2, 'y0': 3}

# Saving Parameters
config = ConfigParser()
config['DEFAULT'] = {'scale': '1',
                     'x0': '2',
                     'y0': '3'}

config['User'] = {}
config['User']['Name'] = 'yuangreg'
with open('params.init', 'w') as f:
    config.write(f)


# Loading Parameters
config.read('params.init')
scale = float(config['DEFAULT']['scale'])
x0 = int(config['DEFAULT']['x0'])
y0 = int(config['DEFAULT']['y0'])
username = config['User']['Name']

print(scale, x0, y0, username)