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
	x_init = 5
	y_init = -.08
	steps = 100
	lr = 1e-1

	#func = opf.Paraboloid
	func = opf.HyperbolicParaboloid

	# GradientDescent, Momentum, RMSprop
	opt_gd = opm.GradientDescent(func,x=x_init,y=y_init)
	opt_mom = opm.Momentum(func,x=x_init,y=y_init)
	opt_rms = opm.RMSprop(func,x=x_init,y=y_init)
	opt_adm = opm.Adam(func,x=x_init,y=y_init)#,beta1=0.1,beta2=0.1)

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
	if False:
		save_path = '/home/hectorsab/Documents/Tesis/content_creation/optimization_methods/ims/hyperbolic.gif'
		vut.animation_2d([opt_gd,opt_mom,opt_rms,opt_adm],x_range=x_range,y_range=y_range,save=True,
			save_path=save_path,labels_loc='upper right',levels=20,interval=60)

	# 3D
	else:
		save_path = '/home/hectorsab/Documents/Tesis/content_creation/optimization_methods/ims/hyperbolic3d.gif'
		vut.animation_3d([opt_gd,opt_mom,opt_rms,opt_adm],x_range=x_range,y_range=y_range,elev=50,azim=235,
			save=True,save_path=save_path)