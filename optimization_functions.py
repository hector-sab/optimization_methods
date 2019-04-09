import numpy as np

class Paraboloid:
	"""
	Square function.

	f(x,y) = \frac{x^2}{a^2} + \frac{y^2}{b^2}

	dx = \frac{2x}{a^2}
	dy = \frac{2y}{b^2}
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

class HyperbolicParaboloid:
	"""
	Saddle surface.

	f(x,y) = x^2 - y^2

	Gradients:

	dx = 2x
	dy = -2y
	"""
	def __init__(self):
		"""
		"""
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
		self.dx = 2*x
		self.dy = -2*y

	def function(self,x,y):
		"""
		Calculates the square of the function.
		"""
		z = np.power(x,2) - np.power(y,2)
		return(z)

class MonkeySaddle:
	"""
	Saddle surface.

	f(x,y) = x^3 - 3xy^2

	Gradients:

	dx = 3x^2 - 3y^2
	dy = -6xy
	"""
	def __init__(self):
		"""
		"""
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
		self.dx = 3*np.power(x,2) - 3*np.power(y,2)
		self.dy = -6*x*y

	def function(self,x,y):
		"""
		Calculates the square of the function.
		"""
		z = np.power(x,3) - 3*x*np.power(y,2)
		return(z)

class Rosenbrock:
	"""
	Vizualization in x_range [-3,3], y_range [-0,4]
	Formulation:

	f(x,y) = (a - x)^2 - b(y - x^2)^2
	
	-----
	(a-x)^2 = a^2 - 2ax + x^2
	(y-x^2)^2 = y^2 - 2x^2y + x^4
	-----

	f(x,y) = a^2 - 2ax + x^2 + by^2 - 2bx^2y + bx^4
	
	Gradients:

	dx = -2a + 2x - 4bxy + 4bx^3
	dy = 2by - 2bx^2
	"""
	def __init__(self,a=1,b=1):
		"""
		"""
		self.dx = None
		self.dy = None

		self.a = a
		self.b = b

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
		self.dx = -2*self.a + 2*x - 4*self.b*x*y + 3*self.b*np.power(x,3)
		self.dy = 2*self.b*y - 2*self.b*np.power(x,2)

	def function(self,x,y):
		"""
		Calculates the square of the function.
		"""
		pt1 = self.a - x
		pt2 = y - np.power(x,2)
		z = np.power(pt1,2) + self.b*np.power(pt2,2)
		return(z)

class Balea:
	"""
	Vizualization in x_range [-4,4], y_range [-4,4]

	Formulation:

	f(x,y) = (1.5 - x + xy)^2 + (2.25 - x + xy^2)^2 + (2.625 - x + xy^3)2

	-----
	(1.5 - x + xy)^2 = 2.25 - 1.5x + 1.5xy - 1.5x + x^2 - x^2y + 1.5xy - x^2y + x^2y^2
	                 = 2.25 - 3x + 3xy + x^2 -2x^2y + x^2y^2

	(2.25 - x + xy^2)^2 = 5.0625 - 2.25x + 2.25xy^2 - 2.25x + x^2 - x^2y^2 + 2.25xy^2 - x^2y^2 + x^4y^4
						= 5.0625 - 5.5x + x^2 + 5.5xy^2 - 2x^2y^2 + x^4y^4

	(2.625 - x + xy^3)2 = 6.890625 - 2.625x + 2.625xy^3 - 2.625x + x^2 - x^2y^3 + 2.625xy^3 - x^2y^3 + x^2y^6
						= 6.890625 - 5.25x + x^2 + 5.25xy^3 - 2x^2y^3 + x^2y^6
	-----


	f(x,y) = 14.203125 - 13.75x + 3x^2 + 3xy - 2x^2y + 5.5xy^2 + 5.25xy^3 - x^2y^2 - 2x^2y^3 + x^2y^6 + x^4y^4
	
	Gradients:

	dx = -13.75 + 6x + 3y - 4xy + 5.5y^2 + 5.25y^3 - 2xy^2 - 4xy^3 + 2xy^6 + 4x^3y^4
	dy = 3x - 2x^2 + 11xy + 15.75xy^2 - 2x^2y - 6x^2y^2 + 6x^2y^5 + 4x^4y^3
	"""
	def __init__(self):
		"""
		"""
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
		self.dx = -13.75 + 6*x + 3*y - 4*x*y + 5.5*np.power(y,2) + 5.25*np.power(y,3) 
		self.dx += -2*x*np.power(y,2) - 4*x*np.power(y,3) + 2*x*np.power(y,6) 
		self.dx += 4*np.power(x,3)*np.power(y,4)

		self.dy = 3*x - 2*np.power(x,2) + 11*x*y + 15.75*x*np.power(y,2) - 2*np.power(x,2)*y 
		self.dy += -6*np.power(x,2)*np.power(y,2) + 6*np.power(x,2)*np.power(y,5)
		self.dy += 4*np.power(x,4)*np.power(y,3)

	def function(self,x,y):
		"""
		Calculates the square of the function.
		"""
		z = 4.203125 - 13.75*x + 3*np.power(x,2) + 3*x*y - 2*np.power(x,2)*y + 5.5*x*np.power(y,2) 
		z += 5.25*x*np.power(y,3) - np.power(x,2)*np.power(y,2) - 2*np.power(x,2)*np.power(y,3) 
		z += np.power(x,2)*np.power(y,6) + np.power(x,4)*np.power(y,4)
		return(z)
