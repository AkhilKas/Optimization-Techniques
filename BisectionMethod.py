import sys #to exit if conditions do not meet

#Accepting lower bound of interval
a = float(input("Enter lower limit of interval : "))

#Accepting upper bound of interval
b = float(input("Enter upper limit of interval : "))

#Relative error
epsilon = 0.0001

def function(x):

    #function for which minimum point has to be found
    return x**2 + 54/x

def derivative(x):

    #Derivative of function for which minimum value is being found
    return 2*x - 54/(x*x)

def bisection(x, y):

    z = (x + y)/2 #finding mid-point

    #Checking if interval brackets the minimum point
    if derivative(a)*derivative(b) < 0:
        z = (x + y)/2

    #If condition fails, we will not proceed forward
    else:
        sys.exit("The assumed interval doesn't bracket the minimum point")

    #If derivative(z) is 0, then z is minimum point
    if derivative(z) == 0:
        sys.exit("Minimum point is : "+str(z))

    #Continue as long as the value is greater than relative error
    while not (abs(derivative(z)) < epsilon):

        #Calculate mid-point each time
        z = (x + y)/2

        #If derivative(z) > 0 then, right side of minimum has to be reduced
        if derivative(z) > 0:
            y = z

        #If derivative(z) < 0 then, left side of minimum has to be reduced
        if derivative(z) < 0:
            x = z

        #If derivative(z) is 0, then z is minimum point
        if derivative(z) == 0:
            break

    #If derivative(z) == 0, that is minimum point
    print("Minimum point is : "+str(round(z,5)))

bisection(a, b)
