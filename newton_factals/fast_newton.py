# Chris Harshaw
# August 2015
#

import numpy as np 
from cmath import *
from PIL import Image
from time import time

# computes polynomial derivative
def poly_der(p):
	dp = np.empty(len(p)-1)
	for i in range(len(p)-1):
		dp[i] = p[i]*(len(p)-(1+i))
	return dp

"""============================================================
newton_plot()
	- program 

	INPUTS:
		re 			==> real points in grid (numpy array)
		im 			==> imaginary points in grid (numpy array)
		p 			==> polynomial coefficients (numpy array)
		a 			==> coefficient for generalized Newton
		max_iter	==> maximum number of iterations in Newton's method (int)
		tol 		==> tolerance for convergence (float)
		roots 		==> roots of f (numpy array)
		colors 		==> colors corresponding to roots (list of 3-tuples)
		save_path	==> the relative file path for saving
		disp_time 	==> if TRUE, display time that newton plot takes (false)
	OUTPUTS:
		none (plot is produced and saved)

============================================================"""
def newton_plot(re, im, p, max_iter, tol, roots, colors, save_path, a=1.0, disp_time=False):

	# check that tol is sufficiently small
	for i in range(len(roots)-1):
		for j in range(i+1, len(roots)):
			if abs(roots[i]-roots[j]) <= tol:
				print "Error: roots " + str(i) + " and " + str(j) + " are within tolerance distance"
				return

	# set divergence test value
	div_val = 1e35

	# get derivative polynomial
	dp = poly_der(p)

	# record run time
	if disp_time:
		start = time()

	# create 2D array of complex numbers
	Re, Im = np.meshgrid(re, im)
	Z = Re + 1j*Im

	# create array for roots and iter_num
	con_root = -1*np.ones(Z.shape) # initialze -1: diverge
	con_num = max_iter*np.ones(Z.shape)
	iter_reached = max_iter
	
	# for the maximum number of iterations
	for i in range(max_iter):
		
		# update newton step
		Z -= a * ( np.polyval(p,Z) / np.polyval(dp,Z))

		# check for divide by zero errors (divergence)
		div = np.where(abs(Z) == np.inf)
		con_num[div] = i 
		Z[div] = np.nan # stop tracking this point

		# check for divergence
		div = np.where(abs(Z) >= div_val)
		con_num[div] = i
		Z[div] = np.nan # stop tracking this point

		# check for convergence, record root
		for j in range(len(roots)):
			root_ind = np.where(abs(Z - roots[j]) < tol)
			con_root[root_ind] = j
			con_num[root_ind] = i
			Z[root_ind] = np.nan # stop tracking this point

		# break if all points have converged or diverged
		if np.all(np.isnan(Z)):
			iter_reached = i
			break

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

	# create image
	data = [(0,0,0)]*(len(re)*len(im))
	colors = np.array(colors)
	max_shade = float(np.max(con_num[np.where(con_root>=0)]))
	for i in range(len(im)):
		for j in range(len(re)):
			root_num = con_root[i,j]
			shade = float(max_shade - con_num[i,j]) / max_shade
			if root_num == -1:
				data[i*len(re) + j] = (0,0,0)
			else:
				col = np.round(colors[root_num,:]*shade)
				col = col.astype('int')
				data[i*len(re) + j] = tuple(col)
	
	img = Image.new("RGB", (len(re),len(im)))
	img.putdata(data)
	img.save(save_path)

