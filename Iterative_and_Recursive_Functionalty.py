# 4! = 1*2*3*4 = 24
# Factorial using an iterative function
print("factorial results using an interative function")

numbers = [0, 5, 10, 25, 50, 100]

for n in numbers:
    result = 1
    for i in range(1, n + 1):
        result *=i
    print(F"{n}! = {result}")

# Recursive factorial calculation 
def factorial_recursive (n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive (n - 1)
    
for n in numbers:
    print(f"{n}! = {factorial_recursive(n)}")










