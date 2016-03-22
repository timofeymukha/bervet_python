import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def main():
    part1()
    part2()
    part3()


def integrand(y,w, D=20):
    p = 62.5
    return p*(D-y)*w


def w(y):
    return 40-20*np.exp(-(0.01*y)**2)


def adaptiveTrapz(f, a, b, args=(), tol=0.5e-4):
    """adaptiveTrapz adaptively calculates the integral of f from
    a to b, args are extra arguments for f.

    Returns the value of the integral, an approximation of the error and the step size used.
    """

    N = 4; # Number of intervals

    x, h = np.linspace(a, b, N+1 , retstep=True)
    I = np.trapz(f(x,*args), x)

    err = np.inf
    while abs(err) > tol:
        N = 2*N
        x, h = np.linspace(a, b, N+1 , retstep=True)

        I2 = I
        I = np.trapz(f(x,*args), x)


        err = (I-I2)/3

    return I, err, h


def part1():
    print("### PART 1")
    y = np.array([0, 5, 10, 15, 20])
    w = np.array([20.00, 20.05, 20.25, 20.51, 21.18])
    I = np.trapz(integrand(y,w),y)

    print("The hydrostatic pressure is {:.3g}".format(I))

def part2():
    print("### PART 2")

    def hydrostaticPressure(D):
        P, _ = integrate.quad(lambda y: integrand(y, w(y), D),0, D)
        return P

    # Calculate values of the pressure
    N = 100 # Number of points in D to calculate the pressure for
    Ds = np.linspace(10, 100,N)
    Ps = np.zeros(N)

    for i in range(N):
        Ps[i] = hydrostaticPressure(Ds[i])


    # Create figures
    fig = plt.figure(facecolor="white")
    p = plt.plot(Ds,Ps)
    p[0].set_linewidth(2)
    plt.ylim(0, 9e6)
    plt.xlabel("D")
    plt.ylabel("P")

    fig.show()

    fig.savefig("part2.png",format="png")


def part3():
    print("### PART 3")

    def hydrostaticPressure(D):
        P, E, h = adaptiveTrapz(lambda y: integrand(y, w(y), D),0, D)
        return P, E, h


    # Calculate values of the pressure
    N = 100 # Number of points in D to calculate the pressure for
    Ds = np.linspace(10, 100,N)
    Ps = np.zeros(N)
    Es = np.zeros(N)
    hs = np.zeros(N)

    for i in range(N):
        Ps[i], Es[i], hs[i] = hydrostaticPressure(Ds[i])


    # Create the figures
    f, ax = plt.subplots(3, sharex=True)

    pl = [];
    pl.append(ax[0].plot(Ds,Ps, linestyle='-', marker='None')[0])
    pl.append(ax[1].plot(Ds,Es, linestyle='-', marker='None')[0])
    pl.append(ax[2].plot(Ds,hs, linestyle='None', marker='.')[0])

    [p.set_linewidth(2) for p in pl]

    ax[0].set_ylabel("P")
    ax[1].set_ylabel("e")
    ax[2].set_ylabel("h")
    ax[2].set_xlabel("D")

    f.show()

    f.savefig("part3.png",format="png")


if __name__ == "__main__":
    main()