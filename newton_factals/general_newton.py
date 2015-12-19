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
    Z = Re + 1j * Im

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


def newton_method(Z, f_val, df_val, params, max_iter=50, tol=1e-5, div_val=1e35, a=1.0, disp_time=True, known_roots=None):
    # record run time
    if disp_time:
        start = time()

    # put in different form for increased computation speed
    im_num, re_num = Z.shape
    total_num = re_num * im_num
    ind = np.arange(total_num)
    Z_old = np.reshape(Z, (total_num))

    # create array for roots and iter_num
    con_val = np.nan * np.ones(Z_old.shape, dtype=complex)  # initialze NaN: diverge
    con_num = max_iter * np.ones(Z_old.shape)
    iter_reached = max_iter

    # for the maximum number of iterations
    for i in range(max_iter):

        # print iteration
        if disp_time:
            print 'Iteration ' + str(i+1)

        # update newton step
        Z_new = Z_old - a * (f_val(Z_old, **params) / df_val(Z_old, **params))

        # check for divergence
        div = np.array(np.where(abs(Z) >= div_val))  # note: covers divide by zero errors
        con_num[ind[div]] = i

        # check for convergence
        con = np.array(np.where(abs((Z_old - Z_new) / Z_new) < tol))
        con_val[ind[con]] = Z_new[con]
        con_num[ind[con]] = i

        # update iterate
        Z_old = Z_new

        # remove converged and diverged points
        mask = np.ones(Z_old.shape, dtype=bool)
        mask[div] = 0
        mask[con] = 0
        Z_old = Z_old[mask]
        ind = ind[mask]

        # break if all points have converged or diverged
        if Z_old.size == 0:
            iter_reached = i
            break

    # reshape arrays and create one to store root numbers
    con_num = con_num.reshape((im_num,re_num))
    con_val = con_val.reshape((im_num,re_num))
    con_root = np.nan * np.ones((im_num, re_num))

    # determine roots of function
    if known_roots is not None:
        for j in range(len(known_roots)):
            root_ind = np.where(abs(con_val - known_roots[j]) < tol)
            con_root[root_ind] = j
        roots_found = np.unique(con_root[np.where(np.isfinite(con_root))])
        roots_found = roots_found.astype('int')
        roots = known_roots[roots_found]
    else:
        roots_list = []
        for i in range(im_num):
            for j in range(re_num):
                val = con_val[i, j]
                if not np.isnan(val):
                    new_root = True
                    for r in range(len(roots_list)):
                        if abs(val - roots_list[r][0]) < 10 * tol:
                            con_root[i, j] = r
                            roots_list[r].append(val)
                            new_root = False
                            break
                    if new_root:
                        roots_list.append([val])
        roots = np.empty(len(roots_list))
        for i in range(len(roots_list)):
            roots[i] = np.mean(np.array(roots_list[i]), dtype='complex')

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


def newton_plot(con_root, con_num, colors, save_path=None):

    # get number of real and imaginary points
    im_num, re_num = con_root.shape

    # create image
    data = [(0, 0, 0)] * (re_num * im_num)
    c_num = len(colors)
    colors = np.array(colors)

    max_shade = float(np.max(con_num[np.where(np.isfinite(con_root))]))
    for i in range(im_num):
        for j in range(re_num):
            root_num = con_root[i, j]
            if np.isnan(root_num):
                data[i * re_num + j] = (0, 0, 0)
            else:
                shade = float(max_shade - con_num[i, j]) / max_shade
                col = np.round(colors[root_num % c_num, :] * shade)
                col = col.astype('int')
                data[i * re_num + j] = tuple(col)
    img = Image.new("RGB", (re_num, im_num))
    img.putdata(data)

    # return an image if save path is given
    if save_path:
        img.save(save_path)

    # return the image object
    return img
