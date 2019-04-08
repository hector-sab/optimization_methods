"""
Plots the 3D surface and its corresponding countours in the same figure.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import optimization_functions as opf

if __name__=='__main__':
	fig = plt.figure()
	ax = fig.add_subplot(111,projection='3d')
	plt.gca().set_aspect('equal', adjustable='box')

	function = opf.Balea()

	x,y = np.meshgrid(np.linspace(-4,4,20),np.linspace(-4,4,20))

	z = function.function(x,y)

	cmap = "coolwarm" # autumn_r
	ax.plot_surface(x,y,z,cmap=cmap)
	offset = np.amin(z) -10
	cs = ax.contourf(x,y,z,levels=15,cmap=cmap,offset=offset)

	#cbar = fig.colorbar(cs,orientation='horizontal')

	plt.xlabel('X')
	plt.ylabel('Y')
	# Control initial rotations of the 3d plto
	# elev: Inclination, azim: Rotation
	#ax.view_init(elev=None,azim=0)
	plt.savefig('/home/hectorsab/Documents/Tesis/content_creation/optimization/3d.svg',bbox_inches='tight')
	plt.show()