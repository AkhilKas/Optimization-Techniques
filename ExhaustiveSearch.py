import math 

a = int(input("Enter lower bound: "))
b = int(input("Enter upper bound: "))

n = 100 #number of intermediate points

precision = 10**4 #The number of decimal places we want the answer correct to

delx = abs((b - a)/n) #calculating step value

x1 = a
x2 = x1 + delx
x3 = x2 + delx

#Calculate function value at any particular point
def function(x):
    return x*x + 54/x

while (x3 <= b):
    
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