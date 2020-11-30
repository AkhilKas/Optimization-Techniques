#Accepting interval where minimum is to be searched for the function
a = float(input("Enter lower bound: "))
b = float(input("Enter upper bound: "))

#Relative error
epsilon = 0.0001

#Finding mid-point of interval
xm = (a + b)/2

#Increment or decrement value
L = abs(b - a)

#Calculate fcuntion value at any particular point
def function(x):
    return x*x + 54/x

#For region elimination
x1 = a
x2 = b

#Find the interval containing minimum point
def interval_halving(a, b, x1, x2, xm, L):
    
    #Perform iterations as long as L is not < epsilon (relative error)
    while(abs(L) > epsilon):
        
        x1 = a + L/4
        x2 = b - L/4
        xm = (a + b)/2
        
        #Eliminate region to the right of xm
        if(function(x1) < function(xm)):
            b = xm
            xm = x1
        
        #Eliminate region to the left of xm
        elif(function(x2) < function(xm)):
            a = xm
            xm = x2
        
        #Eliminate boundary points
        else:
            a = x1
            b = x2
        
        #Finding new increment/decrement value
        L = b - a
    
    return "The interval containing the minimum point is (" + str(a) + ", " + str(b) + ")"
    
out = interval_halving(a, b, x1, x2, xm, L)  
print(out)