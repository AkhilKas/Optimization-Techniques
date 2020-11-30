a = float(input("Enter lower bound : "))
b = float(input("Enter upper bound : "))

epsilon = 0.0001

# We normalize x by w = (x - a)/ (b - a)

# After normalization, interval becomes (0, 1)
aw = 0
bw = 1
Lw = 1

# We set k = 1
k = 1

# We use the golden number = 0.618
gn = 0.618

def function(x):
    return (x*x + (54/x))

while !(Lw < epsilon):
    