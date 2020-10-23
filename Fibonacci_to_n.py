def fib(n):
    '''
    Generate fibonacci sequence to inputted N range
    '''
    a = 1
    b = 1
    fib_seq = []
    
    for i in range(n):
        fib_seq.append(a)
        a, b = b, a+b
    
    return fib_seq


fib(15)
