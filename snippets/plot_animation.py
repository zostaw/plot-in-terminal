import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()

# set the three to add transparency
fig.patch.set_alpha(0.)
ax.set_facecolor('None')
ax.axis('off')

rng = np.random.default_rng(19680801)
data = np.array([20, 20, 20, 20])
x = np.array([1, 2, 3, 4])

artists = []
for i in range(20):
    data += rng.integers(low=0, high=10, size=data.shape)
    container = ax.plot(x, data)
    artists.append(container)


ani = animation.ArtistAnimation(fig=fig, artists=artists, interval=400)
# save to gif :)
ani.save(filename="plot_animation.gif", writer="pillow")
