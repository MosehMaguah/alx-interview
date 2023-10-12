#!/usr/bin/env python3
'''
method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
'''

def minOperations(n):
    """
    Returns fewest number of operations needed to result in exactly
    n H characters in the file.
    """
    operations = 0
    mini_operations = 2
    while n > 1:
        while n % mini_operations == 0:
            operations += mini_operations
            n /= mini_operations
        mini_operations += 1
    return operations
