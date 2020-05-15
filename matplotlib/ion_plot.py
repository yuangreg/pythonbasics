import matplotlib.pyplot as plt
import numpy as np

X = np.random.rand(20)
Y = np.random.rand(20)

# New figure and set iteractive mode
plt.figure()
plt.ion()

# Set plot parameters
plt.title("Matplotlib ION Mode")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
ax = plt.gca() # gca = 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))

def rotate_data(X, Y, angle = np.pi/10, scale = 0.95):
    X_new = scale*(np.cos(angle)*X - np.sin(angle)*Y)
    Y_new = scale*(np.sin(angle)*X + np.cos(angle)*Y)
    return X_new, Y_new

for iter in range(41):
    X, Y = rotate_data(X, Y)
    # Clear previous data on the plot
    if 'sca' in globals(): sca.remove()
    if 'textsca' in globals(): textsca.remove()
    sca = plt.scatter(X, Y, s=200, lw=0, c='red', alpha=0.5)
    textsca = plt.text(-1, 1, "Iteration # {}".format(iter))
    plt.pause(0.05)


# off iteractive mode
plt.ioff()
plt.show()
