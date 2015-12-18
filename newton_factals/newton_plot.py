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
def newton_plot(re, im, p, a, max_iter, tol, roots, colors, save_path, disp_time=False):

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

	# create new image and color it black
	img = Image.new("RGB", (len(re),len(im)), (0,0,0) )

	# record run time
	if disp_time:
		start = time()

	# iterate through all grid points
	for m in range(len(re)):
		for n in range(len(im)):

			# create complex number z 
			z = re[m] + 1j*im[n]

			div_flag = False
			iter_count = 1

			# Newton's method
			for i in range(max_iter):

				# compute next iterate
				try:
					z -= a * ( np.polyval(p,z) / np.polyval(dp,z) )
				except ZeroDivisionError:
					div_flag = True 
					break

				# check for divergence
				if abs(z) > div_val:
					div_flag = True
					break

				# check for convergence
				if abs(np.polyval(p,z)) < tol:
					break
				iter_count += 1

			# divergent ==> no color (black)
			if div_flag:
				continue 

			# determine if z converged to a given root of f
			for k in range(len(roots)):
				if abs( roots[k] - z ) < tol:

					# color the image accordingly
					shade = float (max_iter - iter_count) / float (max_iter)
					col = tuple([ int(round(shade*val)) for val in colors[k]] )
					img.putpixel((m,n), col)
					break
	
	if disp_time:
		elapsed = time() - start
		m, s = divmod(elapsed, 60)
		h, m = divmod(m, 60)
		print "Run time: " + "%d:%02d:%02d" % (h, m, s)

	img.save(save_path)

