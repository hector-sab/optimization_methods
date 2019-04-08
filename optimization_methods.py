import numpy as np

class GradientDescent:
	def __init__(self,function,x=None,y=None):
		"""
		Args:
		 - function (): Function from optimization_functions 
		     to optimize location.
		 - x,y (int|float): Initial location.
		"""
		self.name = 'GradientDescent'
		self.function = function()

		# Store the progress of the optimization, but 
		# it has to be initialized from set_initial_coord
		self.xs = None
		self.ys = None
		self.zs = None

		self.set_initial_coord(x,y)

	def set_initial_coord(self,x,y):
		"""
		Sets the initial coords to look for the minimum
		"""
		self.x = x
		self.y = y

		self.xs = []
		self.ys = []
		self.zs = []

	def optimize(self,steps=0,lr=0.1):
		"""
		Optimize the location for "steps" steps.
		"""
		for i in range(steps):
			#self.function.function()
			
			loss = self.function.calculate(self.x,self.y)

			self.xs.append(self.x)
			self.ys.append(self.y)
			self.zs.append(loss)

			dx = self.function.dx
			dy = self.function.dy

			self.x = self.x - lr*dx
			self.y = self.y - lr*dx

class Momentum:
	def __init__(self,function,x=None,y=None,beta=0.1):
		"""
		Args:
		 - function (): Function from optimization_functions 
		     to optimize location.
		 - x,y (int|float): Initial location.
		"""
		self.name = 'Momentum'
		self.function = function()
		self.beta = beta
		self.vx = 0
		self.vy = 0

		# Store the progress of the optimization, but 
		# it has to be initialized from set_initial_coord
		self.xs = None
		self.ys = None
		self.zs = None

		self.set_initial_coord(x,y)

	def set_initial_coord(self,x,y):
		"""
		Sets the initial coords to look for the minimum
		"""
		self.x = x
		self.y = y

		self.xs = []
		self.ys = []
		self.zs = []

	def optimize(self,steps=0,lr=0.1):
		"""
		Optimize the location for "steps" steps.
		"""
		for i in range(steps):
			#self.function.function()

			loss = self.function.calculate(self.x,self.y)

			self.xs.append(self.x)
			self.ys.append(self.y)
			self.zs.append(loss)

			# Direction of gradients
			self.vx = self.beta*self.vx + (1-self.beta)*self.function.dx
			self.vy = self.beta*self.vy + (1-self.beta)*self.function.dy

			self.x = self.x - lr*self.vx
			self.y = self.y - lr*self.vy


class RMSprop:
	def __init__(self,function,x=None,y=None,beta=0.1):
		"""
		Args:
		 - function (): Function from optimization_functions 
		     to optimize location.
		 - x,y (int|float): Initial location.
		"""
		self.name = 'RMSprop'
		self.function = function()
		self.beta = beta
		self.sx = 0
		self.sy = 0

		# Store the progress of the optimization, but 
		# it has to be initialized from set_initial_coord
		self.xs = None
		self.ys = None
		self.zs = None

		self.set_initial_coord(x,y)

	def set_initial_coord(self,x,y):
		"""
		Sets the initial coords to look for the minimum
		"""
		self.x = x
		self.y = y

		self.xs = []
		self.ys = []
		self.zs = []

	def optimize(self,steps=0,lr=0.1):
		"""
		Optimize the location for "steps" steps.
		"""
		for i in range(steps):
			#self.function.function()

			loss = self.function.calculate(self.x,self.y)

			self.xs.append(self.x)
			self.ys.append(self.y)
			self.zs.append(loss)

			# Direction of gradients
			dx = self.function.dx
			dy = self.function.dy

			self.sx = self.beta*self.sx + (1-self.beta)*np.power(dx,2)
			self.sy = self.beta*self.sy + (1-self.beta)*np.power(dy,2)

			self.x = self.x - lr*(dx/(np.sqrt(self.sx)+np.finfo(float).eps))
			self.y = self.y - lr*(dy/(np.sqrt(self.sy)+np.finfo(float).eps))

class Adam:
	def __init__(self,function,x=None,y=None,beta1=0.1,beta2=0.1):
		"""
		Args:
		 - function (): Function from optimization_functions 
		     to optimize location.
		 - x,y (int|float): Initial location.
		"""
		self.name = 'Adam'
		self.function = function()
		self.beta1 = beta1
		self.beta2 = beta2
		self.vx = 0
		self.vy = 0
		self.vx_corr = 0
		self.vy_corr = 0

		self.sx = 0
		self.sy = 0
		self.sx_corr = 0
		self.sy_corr = 0

		self.it = 1

		# Store the progress of the optimization, but 
		# it has to be initialized from set_initial_coord
		self.xs = None
		self.ys = None
		self.zs = None

		self.set_initial_coord(x,y)

	def set_initial_coord(self,x,y):
		"""
		Sets the initial coords to look for the minimum
		"""
		self.x = x
		self.y = y

		self.xs = []
		self.ys = []
		self.zs = []

	def optimize(self,steps=0,lr=0.1):
		"""
		Optimize the location for "steps" steps.
		"""
		for i in range(steps):
			#self.function.function()

			loss = self.function.calculate(self.x,self.y)

			self.xs.append(self.x)
			self.ys.append(self.y)
			self.zs.append(loss)

			# Direction of gradients
			dx = self.function.dx
			dy = self.function.dy

			self.vx = self.beta1*self.vx + (1-self.beta1)*dx
			self.vy = self.beta1*self.vy + (1-self.beta1)*dy

			self.vx_corr = self.vx/(1-np.power(self.beta1,self.it))
			self.vy_corr = self.vy/(1-np.power(self.beta1,self.it))

			self.sx = self.beta2*self.sx + (1-self.beta2)*np.power(dx,2)
			self.sy = self.beta2*self.sy + (1-self.beta2)*np.power(dy,2)

			self.sx_corr = self.sx/(1-np.power(self.beta2,self.it))
			self.sy_corr = self.sy/(1-np.power(self.beta2,self.it))

			self.x = self.x - lr*(self.vx_corr/(np.sqrt(self.sx_corr)+np.finfo(float).eps))
			self.y = self.y - lr*(self.vy_corr/(np.sqrt(self.sy_corr)+np.finfo(float).eps))

			# Count of the current iteration
			self.it += 1