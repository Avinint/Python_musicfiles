# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
 
import timeit
from statistics import mean, stdev


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

res = timeit.repeat("fact(200)", setup="from __main__ import fact", number=1000, repeat=6)
res2 = timeit.repeat("factorial(200)", setup="from __main__ import factorial", number=1000, repeat=6)
print(f"Iterative: {mean(res)} {stdev(res)}")
print(f"Recursive: {mean(res2)} {stdev(res2)}")
