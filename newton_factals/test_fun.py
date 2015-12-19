# Chris Harshaw
# December 2015
#

import numpy as np

def sine_fun(Z, **params):
	return np.sin(Z) - 1

def d_sine_fun(Z, **params):
	return np.cos(Z)

def poly_fun(Z,**params):
	return np.polyval(params['p'],Z)

def d_poly_fun(Z,**params):
	return np.polyval(params['dp'],Z)

def htrig_fun(Z, **params):
	return Z * np.sinh(Z) - np.cosh(Z) + 1

def d_htrig_fun(Z, **params):
	return np.sinh(Z)

# computes polynomial derivative
def poly_der(p):
	dp = np.empty(len(p)-1)
	for i in range(len(p)-1):
		dp[i] = p[i]*(len(p)-(1+i))
	return dp