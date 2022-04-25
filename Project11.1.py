"""
File: Project 11.1
Josue Marante 

1. A sequential search of a sorted list can halt when 
the target is less than a given  element in the list. 
Define a modified version of this algorithm, and state 
the  computational complexity, using big-O notation, 
of its best-, worst-, and averagecase performances. 

"""



def  sequentialSearch( target, lyst):
    i = 0
    while i < len(lyst)-1:
        if lyst[i] == target:
            return i
        elif lyst[i] > target:
            return - 1
            i += 1 
        return -1 






"""
Best case: Occurs when the target element is at the index of the list.
In this case, this algorithm would take O(1)time

Average Case: element may occur at the start or in the middle of the list 
or does not excist and its greater than the elements in the start of the list. 
In this case, This algorithm would take O(n)time

Worst case: The target element may exist at the end of the list or does not
exist. If the element is greater than the end element then it would take 
O(n)
"""
