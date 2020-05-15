import matplotlib.pyplot as plt
import numpy as np
import cv2

plt.figure(1)
# plt.subplot(n_rows, n_cols, plot_num)
plt.subplot(4, 5, (5, 10))
# figure splits into 4 rows, 5 cols, plot to (4 - 10 subfigures) as shown below
'''
_____________________
| 1 | 2 | 3 | 4 | 5 |
---------------------
| 6 | 7 | 8 | 9 | 10|
---------------------
| 11| 12| 13| 14| 15|
---------------------
| 16| 17| 18| 19| 20|
---------------------
'''

# Scatter Plot
n = 256    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
color = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, c=color, alpha=0.5)
plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks
plt.title("scatter plot")

# Bar plot
plt.subplot(4, 1, 4)
n = 6
X = np.arange(n)
Y1 = np.random.uniform(0.2, 1.0, n)
Y2 = np.random.uniform(0.2, 1.0, n)

plt.bar(X, +Y1, color='b', edgecolor='white')
plt.bar(X, -Y2, color='r', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, y, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, -y, '%.2f' % y, ha='center', va='top')

plt.xlim(-1, n)
plt.xticks(np.linspace(0, n-1, n))
plt.ylim(-1.25, 1.25)
plt.yticks(())
plt.title("Bar plot")


# Contour plot
plt.subplot(4, 5, (13, 15))
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

# add contour field
plt.contourf(X, Y, f(X, Y), 8, alpha=.75)
# Add colorbar
plt.colorbar()
# add contour lines
C = plt.contour(X, Y, f(X, Y), 4, colors='black')
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.title("contour plot")


# Image Show
plt.subplot(4, 5, (1, 7))
image = cv2.imread('./matlibplot_names.png')
plt.imshow(image)
plt.xticks(())
plt.yticks(())
plt.title("show image")


# Secondary y-axis
x = np.arange(0, 10, 0.1)
y = 0.05 * x**2

ax1 = plt.subplot(5, 7, (4, 12))
plt.title("Two Y Axis")

ax2 = ax1.twinx()    # mirror the ax1
ax1.plot(x, y, 'g-')
ax2.plot(x, -y, 'b-')

ax1.set_xticks(())
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')



# Finally show image
plt.show()