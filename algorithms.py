# Why analyze algorithms?
#   - Procedure or formula for solving a problem
#   - Some are so useful that they have names:
#       - Binary search
#       - Bubble sort
#       - Insertion sort
#       - Merge sort
#       - Quick sort
#       - Selection sort
#       - Heap sort
#       - Radix sort
#       - etc.

# Imagine i came up with this function:

def sum(n):
    '''
    Take an input of n and return the sum of the numbers 0 to n.     
    '''
    
    #Vairable to hold the sum
    final_sum = 0
    # Loop through each number from 0 to n
    for i in range(n+1):
        final_sum += i
    # return the sum
    return final_sum

def sum2(n):
    '''
    Take an input of n and return the sum of the numbers 0 to n.
    '''
    return n * (n + 1) / 2

print(sum(5))
print(sum2(5))
