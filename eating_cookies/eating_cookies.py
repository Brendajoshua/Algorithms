#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
   # cache solution
   # if n is less than 0, return 0
    if n < 0:
      return 0
    # if there is no cache
    if cache is None:
      # create a cache using a range based loop
      cache = [0 for i in range(n + 1)]
    
    #cache at index 0 is equal to 1
    cache[0] = 1
    # if n is greater than 0
    if n > 0:
      # the cache at index 1 is 1
      cache[1] = 1
    # if n is gretaer than 1
    if n > 1:
      # cache at index 2 is 2
      cache[2] = 2
    # if n is equal to zero
    if cache[n] == 0:
      # set the cache at n to the recursive call passing the cache
      cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    #return cache at n
    return cache[n]

    #non cache solution
   # if n < 0:
     # return 0
    # elif n < 2:
      # return 1
    # else:
      # return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')