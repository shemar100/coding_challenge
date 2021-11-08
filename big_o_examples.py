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

