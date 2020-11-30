# import math

x = []
x.append(1) # initial guess
delta = 0.001 # increment size
k = 0 # keep track of different values of x

# precision = 10**10 #The number of decimal places we want the answer correct to

# Calculate function value at any particular point
def function(x):
    return x*x + 54/x

# we have to check if the choosen delta should be positive or negative
def checkDelta(d):
    if(function(x[0] - d) >= function(x[0]) and function(x[0]) >= function(x[0] + d)):
        return ("Delta is +ve"),0

    elif(function(x[0] - d) <= function(x[0]) and function(x[0]) <= function(x[0] + d)):
        d = -1 * d
        print("Delta is -ve"),1

    else:
        return ("Initial guess is incorrect, choose another value and try again"),-1

def bounding_phase(k):
    
    # Continue to perform iteration until 'if' fails
    while(True):
    
        x.append(x[k] + (2**k)*delta)
    
        if(function(x[k+1]) < function(x[k])):
            k = k + 1
    
        else:
            
             
            print("Minimum point lies in (" + str(x[k-1]) + ", " + str(x[k+1]) + ")")
            return False
    
bounding_phase(k)

'''print("Minimum lies in (" + str(math.trunc((x[k-1]*precision)/precision)) + ", " 
                  + str(math.trunc((x[k+1]*precision)/precision)) + ")")'''