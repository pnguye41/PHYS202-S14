
import numpy as np

def twoPtForwardDiff(x,y):
    """Performs a forward differention on y with respect to x.
    Uses np.diff to forward differentiate points in [0:-1].
    Fills in dy/dx for last y(x) value manually."""
    #specify the size of dy ahead because diff returns an array of n-1 elements
    dydx = np.zeros(y.shape,float) #we know it will be this size
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def twoPtCenteredDiff(x,y):
    """Performs a centered differentiation on y with respect to x.
    Uses center differentiation formula on points in [1:-1].
    Fills in dy/dx for first and last values manually."""
    #calculate dydx by center differencing using array slices
    dydx = np.zeros(y.shape,float) #we know it will be this size
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    return dydx

def fourPtCenteredDiff(x,y):
    """Performs a four-point centered differentiaton on y with respect to x.
    Uses four-point center differentiation method on x,y values in [2:-2].
    Fills in dy/dx manually for first, second, second-to-last, and last values."""
    #calculate dydx by center differencing using array slices
    dydx = np.zeros(y.shape,float) #we know it will be this size
    dydx[2:-2] = (y[0:-4] -8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*(x[2:-2] - x[1:-3])) #center difference
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    dydx[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])
    return dydx