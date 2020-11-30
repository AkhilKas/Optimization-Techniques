x = []
x[0] = 1 #initial guess
delta = 0.001 #increment size
k = 0 #keep track of different values of x

#Calculate function value at any particular point
def function(x):
    return x*x + 54/x

#we have to check if the choosen delta should be positive or negative
def checkDelta(d):
    if(function(x[0] - d) >= function(x[0]) and function(x[0]) >= function(x[0] + d)):
        return ("Delta is +ve"),0

    elif(function(x[0] - d) <= function(x[0]) and function(x[0]) <= function(x[0] + d)):
        d = -1 * d
        print("Delta is -ve"),1

    else:
        return ("Initial guess is incorrect, choose another value and try again"),-1
    
   