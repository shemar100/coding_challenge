# O(1) Constant 
# With algorithms that has a constant time complexity, the growth of the input doen't have a computational intesnity
def func_constant(values):
    '''
    Prints the first items in a list of values.
    '''
    print(values[0])


func_constant([1,2 ,3, 4, 5])

# O(n) Linear
# With algorithms that has a Linear time complexity, the growth of the input has a computational intesnity
def func_linear(data_lst):
    '''
    Prints the first n items in a list of values.
    '''
    for val in data_lst:
        print(val)

func_linear(['a', 'b', 'c', 'd', 'e'])

def comp(lst):
    '''
    This function prints the first item 0(1) it is a costant
    Then it prints the first half of the list
    Then prints a string 10 times 0(10) it is a constant
    '''

    print(lst[0])

    midpoint = len(lst) // 2

    for val in lst[:midpoint]:
        print(val)
    
    for x in range(10):
        print('number')
    
comp(['a', 'b', 'c', 'd', 'e'])

# O(n^2) Quadratic
# With algorithms that has a Quadratic time complexity, the growth of the input has a computational intesnity at a quadratic rate
def func_quadratic(data_lst):
    '''
    Prints the first n items in a list of values.
    '''
    for item1 in data_lst:

        for item2 in data_lst:
            print(item1, item2)
    
func_quadratic(['a', 'b', 'c', 'd', 'e'])

# Worst Case vs Best Case
def matcher(lst, match):
    '''
    For a list lst, return a boolean indicating if match item is in the list.
    '''

    for item in lst:
        if item == match:
            return True
    return False

print(matcher(['a', 'b', 'c', 'd', 'e'], 'a')) # This is the best case because it is the first item in the list at index 0. O(1) Best Case becomes a constant
print(matcher(['a', 'b', 'c', 'd', 'e'], 'l')) # Worst case, entire list must be searched, n elements. O(n) Worst Case becomes linear


# Space complexity
def memory (n=10):
    ''' 
    Prints "hello world n times"
    '''

    for x in range(n): # Time complexity is O(n)
        print('Memory!') # Space complexity is O(1)

memory()