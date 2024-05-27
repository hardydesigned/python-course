# Sudo Random numbers
# Random numbers are generated using a pseudo-random number generator (PRNG) which uses a seed to generate the first random number. If the seed is not specified, the current system time is used. The seed can be specified using the seed() function. The seed() function is useful in cases where you want to generate random numbers that are reproducible. For example, you may want to generate random numbers for testing purposes. In such cases, you can set the seed to a fixed value so that the same random numbers are generated every time the program is run.
import random

# Random number between 0 and 1
print(random.random())

mylist = list("ABCDEFGH")
random.shuffle(mylist)
print(mylist)

# Random number between 1 and 10
print(random.randint(1, 10))

print(random.seed(10))

# Gererate truly random numbers

import secrets

print(secrets.randbelow(10))

print(secrets.randbits(4))

# Numpy random numbers for arrays
import numpy as np

print(np.random.rand(3)) # 3 random numbers between 0 and 1

print(np.random.randint(1, 10, 3)) # 3 random numbers between 1 and 10

np.random.seed(10)
print(np.random.rand(3))

np.random.seed(10)
print(np.random.rand(3))
