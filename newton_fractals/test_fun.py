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

def rational_fun(Z, **params):
    return np.polyval(params['p'], Z) / np.polyval(params['q'], Z)

def d_rational_fun(Z, **params):
    p = params['p']
    dp = params['dp']
    q = params['q']
    dq = params['dq']
    hi = np.polyval(q, Z) * np.polyval(dp, Z) - np.polyval(p, Z) * np.polyval(dq, Z)
    low = np.polyval(q, Z) ** 2
    return hi / low

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

def parameterized_roots1(speeds, num_times):

    N = len(speeds) # number of roots
    speeds = np.array(speeds) # speeds of roots
    G = float(lcmm(speeds)) # shortest period of roots movement

    # parameter t
    t = np.linspace(0, G*np.pi, num=num_times)

    # create distance of each root from origin
    distance = np.cos(np.outer(t,speeds))

    # create rotations for each root
    rotations = np.exp(1j*2*np.pi* np.arange(N, dtype=float) / N).reshape((1,N))

    # rotate distances across unit circle to obtain roots
    param_roots = distance * rotations

    return param_roots

def parameterized_roots2(speeds, num_times):

    N = len(speeds) # number of roots

    # create parameter t
    a1 = np.linspace(0, 1.318, np.floor(float(num_times)/4.0))
    a2 = np.linspace(1.318, 0, np.ceil(float(num_times)/4.0))
    a = np.concatenate((a1,a2))
    t = np.cos(np.concatenate((a,a)))

    # create distance of each root from origin
    distance = np.cos(np.outer(t,speeds))

    # create rotations for each root
    rotations = np.exp(1j*2*np.pi* np.arange(N, dtype=float) / N).reshape((1,N))

    # rotate distances across unit circle to obtain roots
    param_roots = distance * rotations

    # rotate circularly
    circ_rot = np.exp(1j*2*np.pi* np.linspace(0,1, num_times))
    circ_rot = circ_rot.reshape((num_times,1))
    param_roots = param_roots * circ_rot

    return param_roots
