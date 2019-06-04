#!/usr/bin/python

def window(array):

    # The last read element in the array that is greater than the minimum of the array.
    left_bound = None

    # The last read element in the array that is less than the of maximum of the array.
    right_bound = None

    n = len(array)

    # Variables that determine the highest and lowest bounds of the array.
    max_bound = -float("inf")
    min_bound = float("inf")

    for i in range(n):
 
        max_bound = max(max_bound, array[i])

        # If the array elemenet is less than the running maximum
        # set it as the right bound.
        if array[i] < max_bound:    
            right_bound = i

    for i in range(n-1, -1, -1):
        
        min_bound = min(min_bound, array[i])

        # If the array element is greater than the running minimum
        # set it as the left bound.
        if array[i] > min_bound:
            left_bound = i

    # Return the indicies that are in need of sorting as a tuple.
    return left_bound, right_bound

if __name__ == "__main__":
    
    array = [3, 7, 5, 9, 6]
    print array
    print window(array)
