import matplotlib.pyplot as plt
import numpy as np


# setup plot surrounding frames to white (otherwise they look bad with transparent=True)
import matplotlib
matplotlib.rc('axes',edgecolor='white')
matplotlib.rc('axes',facecolor='white')


length = 5
X = np.linspace(0, length, length)

# setup size of the plot
fig, ax = plt.subplots(figsize=(15,8))

ax.plot(X, (0.5*X + 0.1), label="0.5x + 0.1")
ax.plot(X, np.sin(X), label="sin(x)")
# setup colors of the ticks and labels around frames
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
plt.legend()


# ax.axis('off') # or disable axes completely to make zen-mode

# set positions to allow space for frames around plot, otherwise it only prints the inside, but labels are outside of visible space
plt.gca().set_position([0.05, 0.05, 0.95, 0.95])
plt.savefig("plot_png.png", transparent=True)

# then execute:
# kitty icat --align=left artifacts/plot_png.png
