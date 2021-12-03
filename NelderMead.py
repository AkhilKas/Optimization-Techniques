#import numpy, which we will use for are arrays/simplex

import numpy as np



# The function Arranging will be used to sort the points in ascending order according to their function values
def Arranging(x, sorting):
    index_list = np.argsort(sorting)
    return x[index_list], sorting[index_list]


### We define the transformations below that will be performed iteratively in order to move our initial set of points towards the
### direction where the function decreases the most. 

## The first reflection is used to reflect the simplex symmetrically with respect to the centroid x0, which is then shifted when the worst point
### is replaced by its reflection R.
def Reflection(x,R,f_x,function,x0,n_1):
                    x[-1] = R
                    f_x[-1] = function(R)
                    x, f_x = Arranging(x, f_x)
                    x0 = x0 + n_1 * (R - x[-1])
                    return x,f_x,x0
### The second reflection is performed instead when the reflection of the worst point achieves the lowest function value
## Even compared to the value achieved when the reflection is followed by an expansion. Again, the simplex is reflected with respect to the centroid,
### the worst point is removed and the refle       
def Reflection2(x,R,f_x,f_R,x0,n_1):
    x = np.append(R.reshape(1, -1), x[:-1], axis=0)
    f_x = np.append(f_R, f_x[:-1])
    x0 = x0 + n_1 * (R - x[-1])
    return x, f_x, x0 
### When the point E obtained after expansion of the previously reflected point R achieves a lower value than the previous one, we decide to keep the expansion.
### That is, we extend the simplex towards the points that are more likely to decrease the function value. 
### This is done by applying the expanding function to our simplex, range of value, and expanded point E. 
def Expanding(x,f_x,E,f_E,x0,n_1):
    x = np.append(E.reshape(1, -1), x[:-1], axis=0)
    f_x = np.append(f_E, f_x[:-1])
    x0 = x0 + n_1 * (E - x[-1])
    return x, f_x, x0
### Finally, if the intitially reflected point R achieves a greater value than the worst point, but a better value than the point that is then expanded
### This means that the set of optimal points lie in a subset of the previsous simplex, therefore the simplex must be reduced
### This is done either by contraction or shrinkage
### Contraction is performed by moving the worst point closer to the other points in order to reduce the simplex.
def Contraction(x,C,f_x,function,x0,n_1):
    x[-1] = C
    f_x[-1] = function(C)
    x, f_x = Arranging(x, f_x)
    x0 = x0 + n_1 * (C - x[-1])
    return x,f_x,x0
### Shrinkage is done by moving all the points towards the best point x[0], that is reducing the distance between x[0] and all the other points. 
### Again we re-evaluate the centroid obtained. 
def Shrinking(x,f_x,x0,function):
    x[1:] = (1 - sigma) * x[0] + sigma * x[1:]
    f_x[1:] = np.array(list(map(function, x[1:])))
    x, f_x = Arranging(x, f_x)
    x0 = np.mean(x[:-1], axis=0)
    return x,f_x,x0



#Here we define the NelderMead algorithm. It takes 3 arguments: function, simplex, itermax
#function is the function we want to minimize, simplex is the simplex
#simplex is the working simplex that has our vertices. the function does not initialize it, so it has
#to be passed as an arugment to the function, as an np array.
#itermax is the number of iteration the algorithm will do, it can be considered as our termination criteria
def NelderMead(function,simplex,itermax):
    #here we create a variable x and make it equal to the simplex, we then take a variable n and assign to it the number
    #of columns of the simplex. Then we assign to a variable n_1 the inverse of n, as we will use it later
    x = simplex.copy()
    n = x[0].size
    n_1 = 1 / n
    #here we create an array f_x which will contain the images using the function of each vertices of the simplex
    f_x = np.array(list(map(function, x)))
    #Here we sort x and f_x by ascending order in regards to the f_x value.
    x, f_x = Arranging(x, f_x)

    #here we compute the first centroid x0 of all point except xn+1. We thus compute the mean of all points excpet the last one 
    #of x, as x is arranged by ascending order and that we want to minimize f_x
    x0 = np.mean(x[:-1], axis=0)

    #here we set our for loop in order for the algorithm to iterate itermax number of times
    for j in range(itermax):
        #here we assign the best, bad and worst result of our function to respectively f_b, f_B and f_W. As
        #x and f_x are sorted by ascending order, and that we want to minimize, the best is the first element of f_x, the bad
        #is the one before last element of f_x and the worst is the last element of f_x
        f_b = f_x[0] 
        f_B = f_x[-2]
        f_W = f_x[-1]
        #we then assign to W the corresponding worst points
        W = x[-1]

        #here we compute the reflection of the worst point, and its image using R
        R = x0 + alpha * (x0 - W)
        f_R = function(R)

        #Here we check that if the reflected point is better than the bad, but not better than the best, (better meaning smaller
        #as we want to minimize), then we use the Reflection function defined earlier 
        if f_b <= f_R and f_R < f_B:
            x,f_x,x0 = Reflection(x,R,f_x,function,x0,n_1)
        #If the reflected point is the best point so far, we compute the expanded point E and its image
        elif f_R < f_b:
            E = x0 + gamma * (x0 - W)
            f_E = function(E)
            # If the expanded point E is better than point R we use the expansion function defined earlier to replace
            # the worst point W by the expanded point E
            if f_E < f_R:
                x,f_x,x0 = Expanding(x,f_x,E,f_E,x0,n_1)
            # Otherwise we use the reflection function to replace the worst point W by the reflected point R
            else:
                x,f_x,x0 = Reflection2(x,R,f_x,f_R,x0,n_1)

            # In this case, the reflected point is worse than the bad
        else:
            
            # If the reflected point is worse than the worst point W we compute the contracted point C using W
            if f_R > f_W:
                C = x0 + rho * (W - x0)
            else: 
            # If the reflected point is better than the worse point W we compute the contracted point C using R
            # The image of the point W is replaced by the image of the reflected point R
                C = x0 + rho * (R - x0)
                f_W = f_R
            # If the image of the contracted point C is better than the image of the worst point we use the contraction function defined earlier
            # to replace the worst point W with the contracted point C
            if function(C) < f_W:
                x,f_x,x0 = Contraction(x,C,f_x,function,x0,n_1)
            # If the image of the contracted point C is worse than the image of the worst point we use the shrinking function defined earlier
            # to replace all points except the best
            else:
                x,f_x,x0 = Shrinking(x,f_x,x0,function)

    return x, f_x

#We define our main function
def main():
  #Here we define the parameters we will use for the algorithm, we set them as global and set the values as the standards ones
  print("Alpha, gamma, rho and sigma are currently set as the standards ones.\nThey are respectively the reflection, expansion,\
  contraction and shrink coefficients:\nalpha = 1.0\ngamma = 2.0\nrho = 0.5\nsigma = 0.5\nIf you wish to change them, go in the\
 .py file")
  global alpha,gamma,rho,sigma 
  alpha = 1.0
  gamma = 2.0
  rho = 0.5
  sigma = 0.5
  #Here we ask the user to enter the number of max iteration, thus to enter the termination parameter
  itermax = int(input("Enter number of max iteration\n"))
  #The function we will be minimizing (dot product)
  function = lambda x: x @ x
  print("The function you are minimizing is x * x for x in R^n\n")
  #The simplex that was supposed to be initialized 
  simplex = np.array([[0.13,0.08],[0.08,0.13],[0.08,0.08]])  
  print(simplex,"\n")
  print("The current simplex is displayed above, you may change it's dimension and variables inside the .py file\n")
  #Here we run our Nelder Mead algorithm over the previously defined function (dot product), our simplex and the number of 
  #max iteration. As our function NelderMead returns the simplex of optimal x and an array corresponding of their images
  #by the function, we store the result in two variables: optimal_simplex, optimal_value
  optimal_simplex, optimal_value = NelderMead(function, simplex, itermax)
  #We display the result.
  print("optimal_simplex: \n",optimal_simplex,'\n\nopitmal_value:\n', optimal_value)

#Run main function 
if __name__ == "__main__":
  main()