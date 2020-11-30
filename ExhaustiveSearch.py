import math 

a = float(input("Enter lower bound: "))
b = float(input("Enter upper bound: "))

n = 100 # number of intermediate points

precision = 10**4 # The number of decimal places we want the answer correct to

delx = abs((b - a)/n) # calculating step value

x1 = a # assigning x1 to lower bound of interval
# Taking two points with small increments from the lower bound as x2, x3
x2 = x1 + delx 
x3 = x2 + delx

# Calculate function value at any particular point
def function(x):
    
    # Taking a random unimodal function
    return x*x + 54/x

def exhaustive_search(x1, x2, x3):
    # x3 should be <= b, else we will be calculating values outside the specified interval
    while (x3 <= b):
        
        # checking if function changes signs in specified interval
        if(function(x1) >= function(x2) and function(x2) <= function(x3)):
            break
    
        else:
            x1 = x2
            x2 = x3
            x3 = x2 + delx
    
    if(x3 > b):
        print("No minimum exists in (a, b) or a boundary point (a or b) is the minimum point.")
    
    else:
        print("Minimum point lies in the region : (" + str((math.trunc(x1*precision))/precision) + " , " 
          + str((math.trunc(x3*precision))/precision) + ")")
        
exhaustive_search(x1, x2, x3)