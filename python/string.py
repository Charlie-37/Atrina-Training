'''String:- It is a sequence of Character which is enclosed by Quotation mark. Any number, special symbol and alphabet inside quotation mark is considered as a string. In Python the default input is string.'''

# //*---String Operations----*//


# //* 1. Concatination 

str1 = "Hello"
str2 = "World"

#print(str1+" "+ str2)


# //* 2. Replication

#print(str1*10)

# //* 3. Indexing 

# print(str1[2])

# //* 4. Slicing 

# print(str1[0:2])


# //*--------String Methods---------*//


# //* 1. .upper()

# print(str1.upper())

# //*  2.  .lower()

# print(str1.lower())

# //* 3. .capitalize()

# print(str1.capitalize())


# //* 4.  .swap()

# print(str1.swapcase())

# //* 5. replace()

# print(str1.replace('H', 'M'))

# //* 6.  .lstrip()

strls = '    Hello World'

# print(strls.lstrip())

# //*7.  .rstrip()

strrs = 'Hello World      '

# print(strrs.rstrip())



# //* 8. .strip()

strs = '     Hello World      '

# print(strs.strip())


# //* 9. .join()

list1 = ['hello', 'world', 'welcome', 'to', 'python']
print(' '.join(list1))


