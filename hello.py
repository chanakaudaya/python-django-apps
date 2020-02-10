
def fib(n): #Write Fibonacci series up to n
    """ Print a Fibonacci series up to n. """
    a,b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Call the function
fib(10)

words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

for i in range(5,10,2):
    print(i)

for n in range(2,10):
    for x in range (2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
            print(n, 'is a prime number')

def fib2(n):
    """Return a list containing the Fibonacci eries up to n. """
    result = []
    a,b = 0,1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

