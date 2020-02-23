"""

Rochester Institute of Technology, Spring 2020
File   : assign2.py
Author : Brian Zarzuela
Email  : bxz1515 @rit.edu

CSCI 665 Foundations of Algorithms
Assignment 2

"""


def fibPow(n):
    a = 0
    b = 1
    c = 1
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
    return b

    # Driver Code if running as script
if __name__ == '__main__':
    print("Fibonacci of n = 35 is 9227465 and using fibPow() is", fibPow(35))



