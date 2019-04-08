"""
Draws the 2D gradient movement 
"""
import numpy as np
import matplotlib.pyplot as plt

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

class Square:
	"""
	3D square function for steps movement.
	"""
	def __init__(self,a=1,b=1):
		"""
		Args:
		 - a,b (int|float): Curvature controls
		"""
		self.a = a
		self.b = b

		self.dx = None
		self.dy = None

	def calculate(self,x,y):
		"""
		Calculates the square of the function and calculates its gradient.
		This function is intended for single steps. If you want to calculate the
		Z value use the "function" method.
		"""
		self.gradient(x,y)
		z = self.function(x,y)
		return(z)

	def gradient(self,x,y):
		"""
		Calculates the gradient of the function.
		"""
		self.dx = (2*x)/np.power(self.a,2)
		self.dy = (2*y)/np.power(self.b,2)

	def function(self,x,y):
		"""
		Calculates the square of the function.
		"""
		pt1 = np.power(x,2)/np.power(self.a,2)
		pt2 = np.power(y,2)/np.power(self.b,2)
		z = pt1 + pt2
		return(z)



if __name__=='__main__':
	# Creates the mesh
	xs_ind = np.linspace(start=-10,stop=10,num=20)
	ys_ind = np.linspace(start=-10,stop=10,num=20)

	xs,ys = np.meshgrid(xs_ind,ys_ind)

	# Z values of the function
	zs = test_function(xs,ys)

	fig,ax = plt.subplots()
	plt.gca().set_aspect('equal', adjustable='box')
	# Colored contours
	#CS = ax.contour(xs,ys,zs)
	
	# Colored surfaces
	cs = ax.contourf(xs,ys,zs,levels=15,cmap=plt.cm.coolwarm)
	# As image...
	#cs = ax.imshow(zs,cmap=plt.cm.coolwarm)
	
	# Adds labels to rings
	#ax.clabel(cs, inline=1, fontsize=10)
	cbar = fig.colorbar(cs)





	func = Square()
	lr = 0.1

	x = 7
	y = 7

	xs = []
	ys = []
	losses = []
	steps = 20
	for i in range(steps):
		loss = func.calculate(x,y)

		xs.append(x)
		ys.append(y)
		losses.append(loss)

		dx = func.dx
		dy = func.dy

		x = x - lr*dx
		y = y - lr*dx

	# Draw circles to indicate the points of gradient
	#ax.scatter(xs,ys,c='b')

	for i in range(steps-1):
		# xy is the arrow and xytext the init of the arrow
		if True:
			ax.annotate('', xy=(xs[i+1],ys[i+1]), xytext=(xs[i],ys[i]),
				arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
				va='center', ha='center')
		else:
			 plt.arrow(xs[i],ys[i],-(xs[i] - xs[i+1]),-(ys[i] - ys[i+1]),head_width=0.05, head_length=0.1)



	if False:
		print(func.calculate(7,7))
		print(func.dx,func.dy)
		ax.scatter(7,7,c='b')

		ax.annotate('', xy=(6,6), xytext=(7,7),
			arrowprops={'arrowstyle': '->', 'color': 'r', 'lw': 1},
			va='center', ha='center')






	plt.show()