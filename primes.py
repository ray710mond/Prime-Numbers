#This program will print out a list of primes starting from 2
import math
import time

count = 0
upper_bound = 10000
n = 3

primes = [2]
print("First Prime: 2")

while(n < upper_bound):
    running = True
    is_prime = True
    while(running & is_prime):
        for prime in primes:
            if (prime > math.sqrt(n)):
                running = False
            if (n % prime == 0):
                is_prime = False
        running == False
    if is_prime == True:
        primes.append(n)
        count +=1
        print("\nNext Prime: " + str(n))
    n+=1
print("\nNumber of primes in range: " + str(count+1))