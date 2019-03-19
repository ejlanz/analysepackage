def sum_array(array):

    '''Return sum of all items in array'''
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    '''
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
