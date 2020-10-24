def timestable(n):
    '''
    Function times each iteration of 1-9 by n
    '''
    table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for t in table:
        nums = t * n
        print(nums)


timestable(9)
