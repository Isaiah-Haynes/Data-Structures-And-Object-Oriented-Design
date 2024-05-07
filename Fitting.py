from scipy import optimize
#from matplotlib import pyplot as plt

# fitting functions
def const(x, c0, c1=0, c2=0):
    return c0
    pass

def lin(x, c1, c0, c2=0):
    return c1*x + c0
    pass

def quad(x, c0, c1, c2):
    return c2*x**2 + c1*x + c0
    pass
    
def fit_data(func, xdata, ydata):
    # TODO: write some code here
    
    
    params, params_cov = optimize.curve_fit(func, xdata, ydata)
    n = len(params)
    c0 = params[0]
    if n >= 2:
    	c1 = params[1]
    if n >= 3:
        c2 = params[2]
    y_fit = []
    for x in xdata:
        y_fit.append(func(x, c0, c1, c2))
    N = len(ydata)
    sq_error = 0
    for i in range(N):
        sq_error += (ydata[i] - y_fit[i])**2
    mse = (1/N) * sq_error
    rmse = mse**(1/2)
    return params, rmse, y_fit
