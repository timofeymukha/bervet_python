from numpy import *
from matplotlib.pyplot import *

#Del 1
p = 62.5
y = array([0, 5, 10, 15, 20])
w = array([20, 20.05, 20.25, 20.51, 21.18])

I = trapz(p*(20-y)*w, y) # Arguments in different order compared to Matlab

print 'Answer to part 1 is ', I

#Del 2 and 3
def width(y, D):
    p = 62.5
    return p*(D-y)*(40-20*exp(-(0.01*y)**2))

D = arange(10, 101) #D is integer! Can add dtype=float64 as argument to fix.

F = zeros(len(D))
errorvals = zeros(len(D))
hvals = zeros(len(D))
nvals = zeros(len(D))

#error that we will have
tol = 1e-3

for i in range(len(D)):
    # !! Avoiding the . after 2  in the line below
    # leads to a bug due to h being integer, if D is integer
    # No longer so in Python 3 as far I know.
    h = D[i]/2. 
    yh = linspace(0, D[i], D[i]/h+1)
    y2h = linspace(0, D[i], D[i]/(2*h)+1)

    inth = trapz(width(yh, D[i]), yh)
    int2h = trapz(width(y2h, D[i]), yh)
    
    #calculate initial error
    error = abs(inth-int2h)/3
    
    #if the error is two large, decrease h until its ok
    while error > tol:
        
        #reduce step-size
        h = 0.5*h
        
        #the old "h" is now "2h", so reassign
        int2h = inth
        
        #form data points for new h
        yh = linspace(0, D[i], D[i]/h+1)
       
        #compute the integral
        inth = trapz(width(yh, D[i]), yh)
        
        #compute the error
        error = (inth-int2h)/3
    errorvals[i] = error
    F[i] = inth
    hvals[i] = h
    nvals[i] = D[i]/h

figure
subplot(311)
plot(D, errorvals, '-o')
xlabel('D, fot')
ylabel('Error estimate')
subplot(312)
plot(D, hvals,'-o')
xlabel('D, fot')
ylabel('h, fot')
subplot(313)
plot(D, nvals, '-o')
xlabel('D, fot')
ylabel('n')
show()
