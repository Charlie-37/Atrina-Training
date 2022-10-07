'''
List:-  It is an ordered and changeable collection of data object. It is enclosed by square bracket [ ] and separated by comas. List can contain mixture of data type.
'''

# #//*- 1. Indexing

# l1 = ['apple', 'Ball', 'Cat','Dog']

# print(l1[1])


# #//* 2. append

# l1.append('elephent')
# # print(l1)

# # //* 3.  Insert

# l1.insert(2,'Zebra')

# # //* 4. Pop

# l1.pop(2)

# # //* 5. Slicing

# # print(l1[1:])

# # //* 6. Remove

# l1.remove('elephent')

# # //* 7. Extend 

# l2 = [1,2,3,4,50]
# l1.extend(l2)
# print(l1)

# list1 = [1, 2, 3, 4, 5,2,4,5,3,6,3,2,3,2]  
# k=3
# list2 = []
# for i in list1:
#     cou = 0
#     for j in list1:
#         if i == j :
#             cou+=1
#     if cou >= k:
#         list2.append(i)

# list2 = list(set(list2))

# print(list2)


# list1 = [1, 1, 1, 64, 23, 64, 22, 22, 22,2]
# list2 = []
# for i in range(0,len(list1)-2):
#     if list1[i] == list1[i+1] and list1[i] == list1[i+2]:
#         list2.append(list1[i])

# print(list2)


# test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
 
# # printing original list
# print ("The original list is : " + str(test_list))
 
# # initializing substring
# subs = 'Geek'
 
# # using list comprehension + len()
# # Count Strings with substring String List
# res = len([i for i in test_list if i.lower().startswith(subs.lower())])

# print(res)


class B:
    def hello(self):
        x =10
        return x


class A():
    count = 0

    def __init__(self,a):
        self.a = a
        A.count +=1

    def show(self,a):
        x = B()
        return print(a)


obj1 = A()
obj2 = A()
obj3 = A()
obj4 = A()

# obj3.show()

A.show('a','b')



