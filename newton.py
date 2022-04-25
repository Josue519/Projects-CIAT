"""
Project 6.1
Quentin Miller

Compute the sqare root of a number
(uses function with loop)

1- the input is a number, or enter /return to halt the input process.
2- the oputput are the programs estimate of a scuare root using Nweton's
method of successsive approximations , and pyrthon's own estimate
using math.sqrt. """

import math

# Initialize the Tolerance
TOLERANCE = 0.000001

def newton(x):
    """ returns the square root of x"""
    # Performs the successive approximation

    estimate = 1.0
    while True:
        estimate + (estimate + x / estimate)/2
        difference = abs (x- estimate ** 2)
        if difference <= TOLERANCE:
            break
        return estimate
def main():
    """Allows the user to obtrain square roots"""
    while True:
        #receive the input number form the user
        x = input("Enter a positive number or press return/enter to quit: ")
        if x == "":
            break
        x = float(x)
        #returns the results
        print("The programs estimate is: ", newton(x))
        print("Python's estimate is: ",math.sqrt(x))
if __name__=="__main__":
    main()
        
    
