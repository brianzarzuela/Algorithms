"""

Rochester Institute of Technology, Spring 2020
File   : assign1.py
Author : Brian Zarzuela
Email  : bxz1515 @rit.edu

CSCI 665 Foundations of Algorithms
Assignment 1

"""


def fib(n):
    """
    Recursive implementation of retrieving the nth number
    of the Fibonacci sequence given using the definition:
    F0 = 0
    F1 = 1
    F2 = F(n-1) + F(n-2)
    :param n: a position in the Fibonacci sequence
    :return: the sum of the previous two Fibonacci numbers
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibItHelper(n, a, b):
    """
    Recursive implementation of the function f as defined:
    f(0; a, b) = a
    f(1; a, b) = b
    f(n; a, b) = f(n-1; a, b)
    :param n: current index
    :param a: current value
    :param b: accumulator
    :return: accumulative sum of preceding values
    """
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fibItHelper(n - 1, b, a + b)


def fibIt(n):
    """
    Calls on fibItHelper to calculate the value of the nth
    position in the Fibonacci sequence by initializing its
    parameters a to 0 and b to 1.
    :param n: a position in the Fibonacci sequence
    :return: the sum of the previous two Fibonacci numbers
    """
    return fibItHelper(n, 0, 1)


# Driver Code if running as script
if __name__ == '__main__':
    print("Fibonacci of n = 35 using FibIt() is ", fibIt(35))
#    print("Fibonacci of n = 35 using Fib() is ", fib(35))



