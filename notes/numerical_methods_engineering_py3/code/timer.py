# This code will contain functions that can test the run time of input functions

import time


def timer(func, args, n=1):
    """This will be a basic timer function that will determine the amount of
    time it will take to run an input function n times
    Inputs:
        func - This is the input function being timed
        args - This is a list of the arguments that the input function will need
            to run
        n - This is the number to times to run the function with the default
            value being 1"""

    x = range(n)
    start = time.time()
    for i in x:
        func(*args)
    tot_time = time.time() - start

    print("It took %.3f seconds to run the function %d times" % (tot_time, n))
