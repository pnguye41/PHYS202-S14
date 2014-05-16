
import numpy as np

def trapz(func,x,lower_bound,upper_bound,slices):
    """Approximates integral of function 'func' of variable 'x' between lower and upper bounds\
    by summing the areas of N trapezoidal slices of equal widths.
    ***Lower and Upper bound arguments must be of type float, not int.***
    """
    N = slices
    a = lower_bound
    b = upper_bound
    h = (b-a)/N

    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())

    print "Trapezoidal Rule Integral =", I
    return I

def simps(func,x,lower_bound,upper_bound,slices):
    """Approximates integral of function 'func' of variable 'x' between lower and upper bounds\
    by fitting parabolas to the curve and summing the areas of N equal width slices.
    ***Lower and Upper bound arguments must be of type float, not int.***
    """
    N = slices
    a = lower_bound
    b = upper_bound
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a)+func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())

    print "Sumpson's rule Integral =",I
    return I