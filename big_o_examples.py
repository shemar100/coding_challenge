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