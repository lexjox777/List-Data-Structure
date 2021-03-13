# # List items are enclosed in square brackets
# List=[]
# # List are ordered
# List=[1,2,3]
# # list are mutable
# List =['orange','apple','pear','apple','banana']
# List[0]='Cherrie'

# print(List)
# # #List elements do not need to be unique
# # List =['orange','apple','pear','apple','banana']

# # # List can be of different data types
# # List=[1, 'Hello',5.0]

# # # =========================
# '''
# List Indexing
# '''
# # fruits =['orange','apple','pear','apple','banana']
# # print(fruits[2])
# # print(fruits[-2])

#   # List within a list 
# # fruits =['orange','apple',['pear','apple','banana']]
# # print(fruits[2][1])

# '''
# Slicing list in python
# '''
# fruits =['orange','apple','pear','apple','banana']
# # print(fruits[:])
# # #  this list all the items in fruits [:]
# # print(fruits[2:5])
# # this slice it where 2 is index and 5 is position i.e it sliced out orange and apple'0-1' Index

# print(fruits[:-3])
# # this sliced out the list backwards

# print(fruits[:3])

# # this sliced out from the beginnng to the third position 'orange','apple','pear'

# print(fruits[2:])

# # this start from index 2 to the last position in the list i.e pear','apple','banana'

# print(fruits[::2])

# #  this skips every other value in the List ['orange','pear','banana']

# print(fruits[::-1])
# # this gives it in a reverse mode 


# '''
# Add Elements to a list 
# '''
# fruits=['orange','apple','pear','apple','banana']
# # fruits[0]='Berries'
# # print(fruits)

# fruits[1:4]=['Pinneaples','Peaches','Plums']
# print(fruits)

# fruits.append('Limes')
# print(fruits)
# append adds elements to a list
'''
Remove or Delete list items
'''

# # fruits =['orange','apple','pear','apple','banana']

# del fruits[0]
# print(fruits)
# del fruits[1:4]
# print(fruits)
# del fruits
# print(fruits)

# using del fruits wont delete all the items in a List except by using del fruits[int] where int is number

'''
Python List Methods
'''
# dir gives all attribute an object has
# print(help(dir))
# print(dir(list))
# print(help(list.index))
# print(help(list.count))
# print(dir(set))

# fruits =['orange','apple','pear','apple','banana']
# fruits.append('cashew')
# print(fruits)

#==================
# fruits =['orange','apple','pear','apple','banana']
# fruits.insert(1,'guava')
# print(fruits)

#======================
# fruits =['orange','apple','pear','apple','banana']
# fruits.clear()
# print(fruits)

#===============
# fruits =['orange','apple','pear','apple','banana']
# fruits.pop(1)
# print(fruits)
# # this popped out the item from the list
# #===============
# fruits =['orange','apple','pear','apple','banana']
# print(fruits.index('orange'))
# this count what position the item is in a list

#===============
# fruits =['orange','apple','pear','apple','banana']

# pos=fruits.index('orange')
# fruits.pop(pos)
# print(fruits)

#=================
fruits =['orange','apple','pear','apple','banana']
# print(fruits.count('apple'))
# result={}
# for x in fruits:
#   result[x]=fruits.count(x)
# print(result)
#================

from collections import Counter
print(Counter(fruits))

#================
'''
List Membership Test
'''
fruits =['orange','apple','pear','apple','banana']

print("orange" in fruits)
print('orange' not in fruits)