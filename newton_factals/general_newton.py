# Chris Harshaw
# August 2015
#

import numpy as np 
from PIL import Image
from time import time

def complex_grid(re_lim, re_num, im_lim, im_num):

	# create 2D array of complex numbers
	re = np.linspace(re_lim[0], re_lim[1], num=re_num)
	im = np.linspace(im_lim[0], im_lim[1], num=im_num)
	Re, Im = np.meshgrid(re, im)
	Z = Re + 1j*Im

	return Z

"""============================================================
newton_method()
	- program 

	INPUTS:
		Z 			==> 2D numpy array of complex points
		f_val		==> function to evaluate
		df_val 		==> derivative of function to evaluate
		params		==> dictionary of parameters for function eval
		max_iter	==> maximum number of iterations in Newton's method (int)
		tol 		==> tolerance for convergence
		div_val 	==> tolerance for divergence
		a 			==> coefficient for generalized Newton
		disp_time 	==> if TRUE, display time that newton plot takes (false)
	OUTPUTS:
		roots 		==> computed roots
		con_num 	==> number of iterations for convergence
		con_root 	==> root that the point converged to (numbered 0 to r-1)

============================================================"""
def newton_method(Z, f_val, df_val, params, max_iter=50, tol=1e-5, div_val=1e35, a=1.0, disp_time=True):

	# record run time
	if disp_time:
		start = time()

	# create array for roots and iter_num
	con_val = np.nan*np.ones(Z.shape) # initialze NaN: diverge
	con_root = np.nan*np.ones(Z.shape)
	con_num = max_iter*np.ones(Z.shape)
	iter_reached = max_iter

	# put in different form for increased computation speed
	re_num = len(re)
	im_num = len(im)
	total_num = re_num * im_num
	tmp = np.indices(Z.shape)
	re_ind = np.reshape(tmp[1],(total_num,1))
	im_ind = np.reshape(tmp[0],(total_num,1))
	ind = np.hstack((im_ind,re_ind))
	Z_old = np.reshape(Z,(total_num,1))

	# for the maximum number of iterations
	for i in range(max_iter):
		
		# update newton step
		Z_new = Z_old - a * ( f_val(Z_old, **params) / df_val(Z_old, **params) )

		# check for divergence
		div = np.where(abs(Z) >= div_val) # note: covers divide by zero errors
		con_num[ind[div,:]] = i

		# check for convergence
		con = np.where(abs((Z_old - Z_new) / Z_new) < tol )
		con_val[ind[con,:]] = Z_new[con]
		con_num[ind[con,:]] = i

		# update iterate
		Z_old = Z_new

		# remove converged and diverged points
		mask = np.ones(Z_old.shape,dtype=bool)
		mask[div] = 0
		mask[con] = 0
		Z_old = Z_old[mask]
		ind = ind[mask,:]

		# break if all points have converged or diverged
		if np.sum(Z.shape) == 0:
			iter_reached = i
			break

	# determine roots of function 
	roots = []
	for i in range(im_num):
		for j in range(re_num):
			val = con_val[i,j]
			if not np.isnan(val): 
				new_root = True
				for r in range(len(roots)):
					if abs(val - roots[r]) < 10*tol:
						con_root[i,j] = r
						roots[r].append(val) 
						new_root = False
						break
				if new_root:
					roots.append([val])
	roots = np.array(roots)
	roots = np.mean(roots,axis=1)

	# print timing results
	if disp_time:
		elapsed = time() - start
		m, s = divmod(elapsed, 60)
		h, m = divmod(m, 60)
		print "Run time: " + "%d:%02d:%02d" % (h, m, s)
		if iter_reached == max_iter:
			print "Maximum iteration reached -- " + str(max_iter)
		else:
			print "Last iteration was " + str(i)

	# return results
	return roots, con_root, con_num

"""============================================================
newton_plot()

	INPUTS:
		con_num 	==> number of iterations for convergence
		con_root 	==> root that the point converged to (numbered 0 to r-1)
		colors 		==> colors corresponding to roots (list of 3-tuples)
		save_path	==> the relative file path for saving

	OUTPUTS:
		none (plot is produced and saved)

============================================================"""

def newton_plot(con_root, con_num, colors, save_path):

	# create image
	data = [(0,0,0)]*(re_num*im_num)
	colors = np.array(colors)
	max_shade = float(np.max(con_num[np.where(np.isfinite(con_root))]))
	for i in range(im_num):
		for j in range(re_num):
			root_num = con_root[i,j]
			if np.isnan(root_num):
				data[i*re_num + j] = (0,0,0)
			else:
				shade = float(max_shade - con_num[i,j]) / max_shade
				col = np.round(colors[root_num,:]*shade)
				col = col.astype('int')
				data[i*re_num + j] = tuple(col)
	img = Image.new("RGB", (re_num,im_num))
	img.putdata(data)
	img.save(save_path)