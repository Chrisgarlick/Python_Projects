lst = [1, 2, 3, 4, 21, 1, 2, 5, 7, 1, 23, 7, 8, 9, 6, 4, 7, 8]

# Mean - Add all up and divide by length
total = sum(lst)
amount = len(lst)

mean = total / amount 


# Median - Sort and find middle number
arranged = lst.sort()
amount = len(lst)
median = lst[9]


# Mode - most occuring number 
mode = [[x, lst.count(x)] for x in set(lst)]

