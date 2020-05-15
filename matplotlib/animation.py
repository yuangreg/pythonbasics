import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

X = np.random.rand(20)
Y = np.random.rand(20)
x = np.arange(-2*np.pi, 2*np.pi, 0.01)


def rotate_data(X, Y, angle = np.pi/10, scale = 0.98):
    X_new = scale*(np.cos(angle)*X - np.sin(angle)*Y)
    Y_new = scale*(np.sin(angle)*X + np.cos(angle)*Y)
    return X_new, Y_new

fig = plt.figure()
plt.title("Matplotlib Animation")
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
ax = plt.gca()  # gca = 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


# Create the object to change in the animation
line_obj, = ax.plot(x, np.sin(x))
scatter_obj = ax.scatter(X, Y, s=200, lw=0, c='red', alpha=0.5)
text_obj = ax.text(-1, 1, '')



def animate(i):
    global X, Y
    X, Y = rotate_data(X, Y)
    offsetdata = np.zeros((len(X),2))
    offsetdata[:, 0] = X
    offsetdata[:, 1] = Y
    line_obj.set_data(x, np.sin(x+0.1*i))
    scatter_obj.set_offsets(offsetdata)
    text_obj.set_text('Iteration # {}'.format(i))
    return scatter_obj, text_obj, line_obj

def init():
    # Set plot parameters
    return scatter_obj, text_obj, line_obj

anim = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=True)

anim.save('animation.gif', writer='PillowWriter', fps=30)
#plt.show()