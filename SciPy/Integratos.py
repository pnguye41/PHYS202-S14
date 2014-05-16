
def trapz(func,x,slices,lower_bound,upper_bound):
    """Approximates integral of function between lower and upper bounds by summing \
    the areas of N trapezoidal slices of equal widths.
    """
    N = slices
    a = lower_bound
    b = upper_bound
    h = (b-a)/N

    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())

    print "Trapezoidal Rule Integral =", I

def simps(func,x):
    """Approximates integral of function between lower and upper bounds by fitting parabolas \
    to the curve and summing the areas of N equal width slices.
    """
    N = 10
    a = 0.0
    b = 2.0
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a)+func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())

    print "Sumpson's rule Integral =",I