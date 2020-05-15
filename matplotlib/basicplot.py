import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

# Basic plot
plt.figure()
plt.plot(x, y2, 'bs-', label='line #1')
plt.plot(x, y1, 'r^--', label='line #2')

# set axis limits and label
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('This is x')
plt.ylabel('This is y')

# set sticks
plt.xticks(np.linspace(-1, 2, 5))
plt.yticks([-2, -1, 0, 1.22, 3],
           ['worst', 'bad', 0, 'good', 'best'])

# Set axis position
ax = plt.gca() # gca = 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))

# Set legend
plt.legend() # loc='upper right'

# Set text
plt.text(1, -1, r'$This\ is\ \mu\ \sigma_i\ \alpha_t$', fontdict={'size': 16, 'color': 'r'})

plt.show()