vowels = 'aeiou'
count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u':0}

vow_string = input("Please enter a sentence")

for vowel in vow_string:
    if vowel in vowels:
        if vowel.lower() == 'a':
            count['a'] += 1
        elif vowel.lower() == 'e':
            count['e'] += 1
        elif vowel.lower() == 'i':
            count['i'] += 1
        elif vowel.lower() == 'o':
            count['o'] += 1
        elif vowel.lower() == 'u':
            count['u'] += 1
            
print(f"There is {count['a']} A's in this sentence")
print(f"There is {count['e']} E's in this sentence")
print(f"There is {count['i']} I's in this sentence")
print(f"There is {count['o']} O's in this sentence")
print(f"There is {count['u']} U's in this sentence")
