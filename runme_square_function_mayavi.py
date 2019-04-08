"""
Plots a 3D surface of the square function using mayavi.
"""
import numpy as np
from mayavi import mlab

def test_function(x,y):
	"""
	Paraboloid.
	Args:
	  - x (int|float|np.ndarray):
	  - y (int|float|np.ndarray):
	Returns:
	  - z (int|float|np.ndarray)
	"""
	a = 1 # Curvature control 1
	b = 1 # Curvature control 2
	z = np.power(x,2)/np.power(a,2) + np.power(y,2)/np.power(b,2)
	return(z)


if __name__=='__main__':
	if True:
		# X and Y limits of the axis
		x_lims = [-10,10]
		y_lims = [-10,10]

		# Create mesh
		xs,ys = np.mgrid[x_lims[0]:x_lims[1]+1,y_lims[0]:y_lims[1]+1]

		# Z values of the function
		zs = test_function(xs,ys)


		mlab.figure(bgcolor=(1,1,1))
		mlab.surf(xs,ys,zs,warp_scale='auto')
		#mlab.mesh(xs.T,ys.T,zs.T)
		mlab.show()

	if False:
		x,y,z,value = np.random.random((4,40))
		mlab.figure(bgcolor=(1,1,1))
		mlab.points3d(x,y,z,value)
		mlab.show()
	
	if False:
	
		dphi, dtheta = np.pi/250.0, np.pi/250.0
		[phi,theta] = np.mgrid[0:np.pi+dphi*1.5:dphi,0:2*np.pi+dtheta*1.5:dtheta]
		m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
		r = np.sin(m0*phi)**m1 + np.cos(m2*phi)**m3 + np.sin(m4*theta)**m5 + np.cos(m6*theta)**m7
		x = r*np.sin(phi)*np.cos(theta)
		y = r*np.cos(phi)
		z = r*np.sin(phi)*np.sin(theta)

		# View it.
		mlab.figure(bgcolor=(1,1,1))
		s = mlab.mesh(x, y, z)
		mlab.show()