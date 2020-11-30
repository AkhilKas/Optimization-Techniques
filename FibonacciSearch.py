a = float(input("Enter lower bound : ")) # lower bound 
b = float(input("Enter upper bound : ")) # upper bound

def function(x):
    return (x*x + 54/x) # calculate unimodal function value

L = b - a # used to calculate L*

n = int(input("Enter the number of interations requied : "))
k = 2

def fibonacci(n): # find nth fibonacci value
    a,b = 0,1
    count = 2
    while count<=(n+1):
        c = a + b
        a,b = b,c
        count+=1
    return b
    
while k!=(n+1):
    
    L1 = (fibonacci((n-k)+1)/fibonacci(n+1))*L
    x1 = a + L1
    x2 = b - L1
    
    if(function(x1)>function(x2)):
        a = x1
        
    elif(function(x2)>function(x1)):
        b = x2
        
    k += 1
 
print("The region containing the minimum is : (" + str(round(a,4)) + " , " + str(round(b,4)) + ")")
