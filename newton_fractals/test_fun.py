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
	return np.polyder(p)

def gcd(a, b):
    # Return greatest common divisor using Euclid's Algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Return lowest common multiple
    return a * b // gcd(a, b)

def lcmm(nums):
    # Return lcm of numpy array
    if nums.size == 2:
        a = nums[0]
        b = nums[1]
        return lcm(a, b)
    else:
        a = nums[0]
        b = nums[1:]
        return lcm(a, lcmm(b))

def parameterized_roots(speeds, num_times):

    N = len(speeds) # number of roots
    speeds = np.array(speeds) # speeds of roots
    G = float(lcmm(speeds)) # shortest period of roots movement

    rotations = np.exp(1j*2*np.pi* np.arange(N, dtype=float) / N)
    distance = np.sin(np.linspace(0, G*np.pi, num=num_times))

    param_roots = np.outer(distance, rotations) # roots are columns, parametrized is rows

    return param_roots