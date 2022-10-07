
#//* 1. Write a Python program to get the largest number from a list.

# list1 = [1,3,6,2,8,67,34,66]

# x = list1[0]
# for i in list1:
#     if i>x:
#         x = i
# print(x)


# //*------------------------------***--------------------------*//

''' Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']'''


# list1 = ['abc', 'xyz', 'aba', '1221']
# count  =0
# for i in list1:
#     if len(i) >=2 and i[0] == i[-1]:
#         count+=1

# print(count)

# //*------------------------------***--------------------------*//

'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''

# list1 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# def last(list1):
#     return list1[-1]

# def lsort(list1):
#     return(sorted(list1, key=last))

# print(lsort(list1))
# //*------------------------------***--------------------------*//

'''Write a Python program to remove duplicates from a list. '''
# list1 = [1,3,2,5,2,6,7,2,4,3]

# x = set(list1)
# print(list(x))
# //*------------------------------***--------------------------*//


'''Write a Python program to find the second largest number in a list.'''

# l1 = [1,23,4,6,6,43,7,87,4]

# l2 = set(l1)
# l2 = list(l2)

# def getmax(l2):
#     l3 = sorted(l2)
#     return(l3[-2])

# print(getmax(l2))

# //*------------------------------***--------------------------*//

''' Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''

# Sample_list = ['p', 'q']
# n =5

# i = 1
# l1 = []
# while i<=n:
#     for j in Sample_list:
#         l1.append(j+str(i))
#     i+=1

# print(l1)
# //*------------------------------***--------------------------*//


'''Write a Python program to convert list to list of dictionaries. Go to the editor
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]'''

# l1 = ["Black", "Red", "Maroon", "Yellow"]
# l2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# l3 = [{'color_name': c,'color_code':f}for f,c in zip(l1,l2)]

# print(l3)

# //*------------------------------***--------------------------*//


'''Write a Python program to sort each sublist of strings in a given list of lists. Go to the editor
Original list:
[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]'''

# l1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# result = list(map(sorted,l1))

# print(result)

# //*------------------------------***--------------------------*//

'''Write a Python program to find the maximum and minimum values in a given heterogeneous list. Go to the editor
Original list:
['Python', 3, 2, 4, 5, 'version']
Maximum and Minimum values in the said list:
(5, 2)'''

# l1 = ['Python', 3, 2, 4, 5, 'version']
# l2 = []
# for i in l1:
#     if isinstance(i,int):
#         l2.append(i)

# print((sorted(l2)[-1],sorted(l2)[-0]))

# //*------------------------------***--------------------------*//


'''Write a Python program to remove duplicate dictionary from a given list. Go to the editor
Original list with duplicate dictionary:
[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
After removing duplicate dictionary of the said list:
[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]'''


# l1=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)

# print(l2)

# //*------------------------------***--------------------------*//

'''Write a Python program to check if the elements of a given list are unique or not. Go to the editor
Original list:
[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
Is the said list contains all unique elements!
False
Original list:
[2, 4, 6, 8, 10, 12, 14]
Is the said list contains all unique elements!
True'''

# x1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# x2 = [2, 4, 6, 8, 10, 12, 14]
# [2, 4, 6, 8, 10, 12, 14]

# def check(x):

#     if list(set(x)) == x:
#         return True
#     else:
#         return False

# print(check(x2))
# //*------------------------------***--------------------------*//

''' Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings. Go to the editor
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']'''

# l1 = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# intl = []
# stl = []
# for i in l1:
#     if isinstance(i,int):
#         intl.append(i)
#     elif isinstance(i,str):
#         stl.append(i)

# l2 = [sorted(intl)+sorted(stl)]
# print(l2)

# //*------------------------------***--------------------------*//


'''Write a Python program to sort a given list of strings(numbers) numerically. Go to the editor
Original list:
['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
Sort the said list of strings(numbers) numerically:
[-500, -12, 0, 4, 7, 12, 45, 100, 200]'''

# l1 = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# l2 = sorted([int(x) for x in l1 ])

# print(l2)
# //*------------------------------***--------------------------*//

'''Write a Python program to get the frequency of the elements in a given list of lists. Go to the editor
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
Frequency of the elements in the said list of lists:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}'''

# l1 = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]

# x = [x for k in l1 for x in k]
# freq = {}

# for i in x:
#     if i in freq.keys():
#         freq[i] += 1
#     else:
#         key = i
#         val = 1
#         freq[i] = 1

# print(freq)

      
# //*------------------------------***--------------------------*//

'''Write a Python program to extract every first or specified element from a given two-dimensional list. Go to the editor
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]
Extract every first element from the said given two dimensional list:
[1, 4, 7]
Extract every third element from the said given two dimensional list:
[3, 6, 9]'''


# l1 = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

# def ext(l1):
#     x = [x[0] for x in l1 ]
#     return x

# print(ext(l1))
# //*------------------------------***--------------------------*//

'''Write a Python program to compute the sum of digits of each number of a given list. Go to the editor
Original tuple:
[10, 2, 56]
Sum of digits of each number of the said list of integers:
14
Original tuple:
[10, 20, 4, 5, 'b', 70, 'a']
Sum of digits of each number of the said list of integers:
19
Original tuple:
[10, 20, -4, 5, -70]
Sum of digits of each number of the said list of integers:
19'''


# l1 = [10, 20, -4, 5, -70]
# l2 = []
# for i in l1:
#     if isinstance(i,int):
#         i = abs(i)
#         for j in range(len(str(i))):
#             x1 = str(i)
#             x2 = x1[j]
#             l2.append(int(x2))
# # print(sum(l2))


# def sumd(nums):
#     return sum(int(el) for n in nums for el in str(n) if el.isdigit())

# print(sumd(l1))

# //*------------------------------***--------------------------*//

'''Write a Python program to find the maximum and minimum values in a given list within specified index range. Go to the editor
Original list:
[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
Index range:
3 to 8
Maximum and minimum values of the said given list within index range:
(5, 0)'''

# l1 = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
# def idx(x,y,l1):
#     l2 = l1[x:y+1] 
#     l2 = sorted(l2)
#     return (l2[-1],l2[0])


# print(idx(3,8,l1))

# //*------------------------------***--------------------------*//

'''Write a Python program to join two given list of lists of same length, element wise. Go to the editor
Original lists:
[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
Join the said two lists element wise:
[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
Original lists:
[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
Join the said two lists element wise:
[['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]'''

# l1 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# l2 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]

# l3 = []
# for i,j in zip(l1,l2):
#     l3.append(i+j)

# print(l3)

# print([x+y for x,y in zip(l1,l2)])


# //*------------------------------***--------------------------*//
'''Write a Python program to add two given lists of different lengths, start from right. Go to the editor
Original lists:
[2, 4, 7, 0, 5, 8]
[3, 3, -1, 7]
Add said two lists from left:
[2, 4, 10, 3, 4, 15]
Original lists:
[1, 2, 3, 4, 5, 6]
[2, 4, -3]
Add said two lists from left:
[1, 2, 3, 6, 9, 3]

'''
# l1 = [2, 4, 7, 0, 5, 8]
# l2 = [3, 3, -1, 7]

# if len(l1) > len(l2):
#     y = len(l1)-len(l2)
# elif len(l1) < len(l2):
#     l1,l2 = l2,l1
#     y = len(l1)-len(l2)

# else:
#     y = 0

# added = [x+y for x,y in zip(reversed(l1),reversed(l2))]
# # print(added)
# print(l1[0:y]+added[::-1])
# //*------------------------------***--------------------------*//
'''Write a Python program to remove first specified number of elements from a given list satisfying a condition. Go to the editor
Remove the first 4 number of even numbers from the following list:
[3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
Output:
[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
Original list:
[3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
Remove first 4 even numbers from the said list:
[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]'''

# l1 = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]

# j = 0    
# for i in l1:
#     if i % 2 == 0 and j<4:
#         j+=1
#         l1.remove(i)
# print(l1)

# //*------------------------------***--------------------------*//

'''Write a Python program to find the last occurrence of a specified item in a given list. Go to the editor
Original list:
['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
Last occurrence of f in the said list:
7
Last occurrence of c in the said list:
15
Last occurrence of k in the said list:
14
Last occurrence of w in the said list:
12'''

# l1 = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# idx = -1
# ch = 'f'
# for i in range(len(l1)):
#     if l1[i] == ch:
#         idx = i

# print(idx)

# //*------------------------------***--------------------------*//




class hello:
    def hel(self):
        x = 20
        y = self.dell()

        return x+y

    def dell(self):
        y = 20

        return y


obj = hello()
print(obj.hel())

