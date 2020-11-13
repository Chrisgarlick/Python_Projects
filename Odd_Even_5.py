lst = range(0,100)

def even_nums(lst):
    '''
    If a number is divisible by 5, stated. Otherwise stated if Odd or Even
    '''
    for item in lst:
        if item % 5 == 0:
            print("Divisible by 5!")
        elif item % 2 == 0:
            print("This is EVEN!")
        else:
            print("This is ODD!")
            
            
even_nums(lst)
