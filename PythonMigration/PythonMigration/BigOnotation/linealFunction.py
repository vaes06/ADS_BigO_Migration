

def loop(a):
    counter = 1
    while counter <= a:
        print(counter)
        counter += 1

def containsNeedle(numberlist, needle):
        for item in numberlist:
            if item == needle:
                return True
        return False

def factorial(n):
    if n == 1:
            return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n < 0:
        Exception("n can not be less than zero")
    elif n <= 2:
        return 1
    fibonacci = 0
    previous =1
    penultimate = 0
    for i in range(1,n+1):
        penultimate = fibonacci
        fibonacci = previous + fibonacci
        previous = penultimate
    return fibonacci

def fibonacciCache(n):
    if n < 0:
        Exception("n can not be less than zero")
    if n <= 2:
        fibonaccicache[n] = 1
        fibonaccicache.append(0)
    if fibonaccicache[n] == 0:
        fibonaccicache[n] = fibonacciCache(n-1) + fibonacciCache(n-2)
        fibonaccicache.append(0)
    return fibonaccicache[n]

# Execute Loop
x = loop(40)

# Find needle
needle = 76
p = (10, 18, 29, 1, 0, 75, 79)
found = containsNeedle(p, needle)
print("Number ", needle, "found?", found)

#Factorial
print(factorial(6))

#Fibonacci
nfibonacci = 80
for i in range(1,nfibonacci+1):
    print("fibonacci", i, "=", fibonacci(i))

#FibonacciCache
fibonaccicache = [0, 0, 0]
for a in range(1,nfibonacci+1):
    print("fibonacci", a, "=", fibonacciCache(a))