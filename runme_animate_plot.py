"""
Animates the optimization methods, both in 2d and 3d forms
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d

import optimization_functions as opf
import optimization_methods as opm
import vizualization_utils as vut


if __name__=='__main__':
	x_init = 0
	y_init = 7.5
	steps = 10000
	lr = 1e-1
	func = opf.Paraboloid

	# GradientDescent, Momentum, RMSprop
	opt_gd = opm.GradientDescent(func,x=x_init,y=y_init)
	opt_mom = opm.Momentum(func,x=x_init,y=y_init)
	opt_rms = opm.RMSprop(func,x=x_init,y=y_init)
	opt_adm = opm.Adam(func,x=x_init,y=y_init)

	# Optimize
	opt_gd.optimize(steps=steps,lr=lr)
	opt_mom.optimize(steps=steps,lr=lr)
	opt_rms.optimize(steps=steps,lr=lr)
	opt_adm.optimize(steps=steps,lr=lr)

	#print(opt_mom.xs[-6:])
	#print(opt_mom.ys[-6:])
	#print(opt_mom.zs[-6:])
	
	x_range = [-10,10]
	y_range = [-10,10]
	# 2D
	if True:
		vut.animation_2d([opt_gd,opt_mom,opt_rms,opt_adm],x_range=x_range,y_range=y_range,save=False,
			save_path='/home/hectorsab/Documents/Tesis/content_creation/optimization/hyperbolic.mp4',
			labels_loc='lower left')

	# 3D
	if False:
		vut.animation_3d([opt_gd,opt_mom,opt_rms,opt_adm],x_range=x_range,y_range=y_range,elev=70,azim=-75)