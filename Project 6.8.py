"""
project 6.8
Josue Marante

Difines the printAll function with a trace
before each recursive call the functyion creates
a slice of its nonempty list arguments.
"""

def printAll(seq):
    if seq:
        print(seq, "->" , [0])
        printAll(seq[1:])
        

printAll(list(range(10)))
