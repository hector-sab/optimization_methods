"""
Vizualization utilities
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d

from itertools import zip_longest

def plot_3d_contourf(optimizer,levels=15,elev=None,azim=None,cmap='coolwarm',
	save=False,save_path='',show=True):
	"""
	Plots the 3D and contourf in the same figure
	Args:
	 - optimizer ():
	  - levels (int): How many levels to display in the contourf.
	  - evel (int|float): Inclination of the initial 3D plot.
	  - azim (int|float): Rotatioin of the initial 3D plot.
	  - cmap ():
	"""
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	plt.gca().set_aspect('equal', adjustable='box')

	x,y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))
	z = optimizer.function.function(x,y)

	ax.plot_surface(x,y,z,cmap=cmap)
	offset = np.amin(z) -10
	cs = ax.contourf(x,y,z,levels=levels,cmap=cmap,offset=offset)

	plt.xlabel('X')
	plt.ylabel('Y')

	# Control initial rotations of the 3d plto
	ax.view_init(elev=elev,azim=azim)

	# Saves the 3D plot
	if save:
		plt.savefig(save_path,bbox_inches='tight')

	# Displays the 3D plot
	if show:
		plt.show()

def plot_contour(optimizer,levels=15,cmap='coolwarm',save=False,save_path='',show=True):
	"""
	Plots the contour of the 3D surface
	"""
	fig,ax = plt.subplots()
	plt.gca().set_aspect('equal', adjustable='box')
 
	x,y = np.meshgrid(np.linspace(-10,10,20),np.linspace(-10,10,20))
	z = optimizer.function.function(x,y)

	# Colored surfaces
	cs = ax.contourf(x,y,z,levels=15,cmap=cmap)
	cbar = fig.colorbar(cs)

	plt.xlabel('X')
	plt.ylabel('Y')

	# Saves the 3D plot
	if save:
		plt.savefig(save_path,bbox_inches='tight')

	# Displays the 3D plot
	if show:
		plt.show()

def plot_contour_gradient(optimizer,levels=15,cmap='coolwarm',save=False,save_path='',show=True,
	x_range=[-10,10],y_range=[-10,10]):
	"""
	Plots the contour of the 3D surface and the steps the optimizer took
	"""
	fig,ax = plt.subplots()
	plt.gca().set_aspect('equal', adjustable='box')

	x,y = np.meshgrid(np.linspace(x_range[0],x_range[1],20),np.linspace(y_range[0],y_range[1],20))
	z = optimizer.function.function(x,y)

	# Colored surfaces
	cs = ax.contourf(x,y,z,levels=15,cmap=cmap)
	cbar = fig.colorbar(cs)

	xs = optimizer.xs
	ys = optimizer.ys

	# To avoid slowing down the computer, get an specific amount of sampels
	if len(xs)>100:
		num = len(xs)
		num = int(num/100)
		xs = xs[::num]
		ys = ys[::num]

	for i in range(len(xs)-1):
		# xy is the arrow and xytext the init of the arrow
		ax.annotate('', xy=(xs[i+1],ys[i+1]), xytext=(xs[i],ys[i]),
			arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
			va='center', ha='center')

	plt.xlabel('X')
	plt.ylabel('Y')

	# Saves the 3D plot
	if save:
		plt.savefig(save_path,bbox_inches='tight')

	# Displays the 3D plot
	if show:
		plt.show()



# Animation Classes taken from:
# http://louistiao.me/notes/visualizing-and-animating-optimization-algorithms-with-matplotlib/

class TrajectoryAnimation(animation.FuncAnimation):
	def __init__(self, *paths, labels=[], fig=None, ax=None, frames=None, 
				 interval=60, repeat_delay=5, blit=True, **kwargs):
		if fig is None:
			if ax is None:
				fig, ax = plt.subplots()
			else:
				fig = ax.get_figure()
		else:
			if ax is None:
				ax = fig.gca()

		self.fig = fig
		self.ax = ax
		
		self.paths = paths

		if frames is None:
			frames = max(path.shape[1] for path in paths)
  
		self.lines = [ax.plot([], [], label=label, lw=2)[0] 
					  for _, label in zip_longest(paths, labels)]
		self.points = [ax.plot([], [], 'o', color=line.get_color())[0] 
					   for line in self.lines]

		super(TrajectoryAnimation, self).__init__(fig, self.animate, init_func=self.init_anim,
												  frames=frames, interval=interval, blit=blit,
												  repeat_delay=repeat_delay, **kwargs)

	def init_anim(self):
		for line, point in zip(self.lines, self.points):
			line.set_data([], [])
			point.set_data([], [])
		return self.lines + self.points

	def animate(self, i):
		for line, point, path in zip(self.lines, self.points, self.paths):
			line.set_data(*path[::,:i])
			point.set_data(*path[::,i-1:i])
		return self.lines + self.points

class TrajectoryAnimation3D(animation.FuncAnimation):
    def __init__(self, *paths, zpaths, labels=[], fig=None, ax=None, frames=None, 
                 interval=60, repeat_delay=5, blit=True, **kwargs):

        if fig is None:
            if ax is None:
                fig, ax = plt.subplots()
            else:
                fig = ax.get_figure()
        else:
            if ax is None:
                ax = fig.gca()

        self.fig = fig
        self.ax = ax
        
        self.paths = paths
        self.zpaths = zpaths
        
        if frames is None:
            frames = max(path.shape[1] for path in paths)
  
        self.lines = [ax.plot([], [], [], label=label, lw=2)[0] 
                      for _, label in zip_longest(paths, labels)]

        super(TrajectoryAnimation3D, self).__init__(fig, self.animate, init_func=self.init_anim,
                                                  frames=frames, interval=interval, blit=blit,
                                                  repeat_delay=repeat_delay, **kwargs)

    def init_anim(self):
        for line in self.lines:
            line.set_data([], [])
            line.set_3d_properties([])
        return self.lines

    def animate(self, i):
        for line, path, zpath in zip(self.lines, self.paths, self.zpaths):
            line.set_data(*path[::,:i])
            line.set_3d_properties(zpath[:i])
        return self.lines



def animation_2d(optimizers,levels=12,x_range=[-10,10],y_range=[-10,10],steps=20,
	cmap='coolwarm',labels_loc='upper left',save=False,save_path='',show=True):
	"""
	Args:
	 - optimizers (list): List of optimizers
	 - levels (int): How many levels to display in the contourf.
	 - x_range (list): Limits of the x plot. [x_min,x_max]
	 - y_range (list): Limits of the y plot. [y_min,y_max]
	 - steps (int): Steps in between the limits.
	 - cmap ():
	 - labels_loc (str): Location of the labels in the plot
	"""
	optimizers_name = []
	trajectories = []
	for optimizer in optimizers:
		optimizers_name.append(optimizer.name)

		xs = np.array(optimizer.xs)
		ys = np.array(optimizer.ys)

		trajectories.append(np.vstack((xs,ys)))

	fig,ax = plt.subplots()
	plt.gca().set_aspect('equal', adjustable='box')

	x,y = np.meshgrid(np.linspace(x_range[0],x_range[1],steps),
		np.linspace(y_range[0],y_range[1],steps))
	z = optimizers[0].function.function(x,y)

	# Colored surfaces
	cs = ax.contourf(x,y,z,levels=levels,cmap=cmap)
	# Displays the color bar
	cbar = fig.colorbar(cs)

	# Animates
	anim = TrajectoryAnimation(*trajectories, labels=optimizers_name, ax=ax)

	# Displays the labels
	ax.legend(loc=labels_loc)

	plt.xlabel('X')
	plt.ylabel('Y')

	if save:
		anim.save(save_path, writer='imagemagick', fps=30)

	if show:
		plt.show()

def animation_3d(optimizers,x_range=[-10,10],y_range=[-10,10],steps=20,elev=None,
	azim=None,cmap='coolwarm',labels_loc='upper left',save=False,save_path='',show=True):
	"""
	Args:
	 - optimizers (list): List of optimizers
	 - x_range (list): Limits of the x plot. [x_min,x_max]
	 - y_range (list): Limits of the y plot. [y_min,y_max]
	 - steps (int): Steps in between the limits.
	 - evel (int|float): Inclination of the initial 3D plot.
	 - azim (int|float): Rotatioin of the initial 3D plot.
	 - cmap ():
	 - labels_loc (str): Location of the labels in the plot
	"""
	optimizers_name = []
	trajectories = []
	zpaths = []

	# Get names and trajectories of each method
	for optimizer in optimizers:
		optimizers_name.append(optimizer.name)

		xs = np.array(optimizer.xs)
		ys = np.array(optimizer.ys)
		zs = np.array(optimizer.zs)

		trajectories.append(np.vstack((xs,ys)))
		zpaths.append(zs)

	# Create figure
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	plt.gca().set_aspect('equal', adjustable='box')

	# Data for the surface to be ploted
	x,y = np.meshgrid(np.linspace(x_range[0],x_range[1],steps),
		np.linspace(y_range[0],y_range[1],steps))
	z = optimizers[0].function.function(x,y)

	# Colored surfaces
	ax.plot_surface(x,y,z,cmap=cmap)

	# Animate trajectories
	anim = TrajectoryAnimation3D(*trajectories,zpaths=zpaths,labels=optimizers_name,ax=ax)

	# Displays labels
	ax.legend(loc=labels_loc)

	# Controls rotations
	ax.view_init(elev=elev,azim=azim)

	plt.xlabel('X')
	plt.ylabel('Y')

	if save:
		anim.save(save_path, writer='imagemagick', fps=30)

	if show:
		plt.show()