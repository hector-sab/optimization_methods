import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

import optimization_functions as opf
import optimization_methods as opm
import vizualization_utils as vut

if __name__=='__main__':
	x_init = 2
	y_init = -2
	func = opf.Balea

	# GradientDescent, Momentum, RMSprop
	opt_gd = opm.GradientDescent(func,x=x_init,y=y_init)
	opt_mom = opm.Momentum(func,x=x_init,y=y_init)
	opt_rms = opm.RMSprop(func,x=x_init,y=y_init)

	# Optimize
	opt_gd.optimize(steps=100,lr=1e-5)
	opt_mom.optimize(steps=100,lr=1e-5)
	opt_rms.optimize(steps=100,lr=1e-5)

	#print(opt_gd.xs[-6:])
	#print(opt_gd.ys[-6:])
	#print(opt_gd.zs[-6:])

	vut.plot_contour_gradient(optimizer,x_range=[-4,4],y_range=[-4,4])