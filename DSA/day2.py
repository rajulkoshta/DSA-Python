# DSA Day 2 notes:
# day 2:
#     copy and updation : id() , same data, s[:]
#     list
#     a = [1,2,3,4]
#     b = ["asd", 2 , True]
#     changing a list : cant change a string
#     a + b = [1,2,3,4,"asd",2,True]
#     c = a : referring to the same data
#     append()
#     list slicing : same as string 
#     but 
#         chaning slice of list[2:4] = [0,3]
#         deleting slice of list[2:4] = []
#     nested lists : [ [1, 2], [2, 3], [3, 4]], [[1,2,3], 4, 9.991, "walkie talkie"]
#     mutable immutable
#     if else elif
#     loops : why?
#     for loop
#     range
#     while loop
#     break & continue


# (https://www.youtube.com/watch?v=mIk8CNJz1H0)
# (https://www.youtube.com/watch?v=kcntdkydPCE)

# THA 2:
#     learn split() function: https://www.w3schools.com/python/ref_string_split.asp
#     learn join() function: https://www.w3schools.com/python/ref_string_join.asp
#     learn list.insert()
#     revise all of this (this being lecture 2 material)
#---------------------------------------------------------------------------------------------------

# Split method

# txt = "welcome to the jungle"
# x = txt.split()
# print(x)

# txt = "hello , my nam is samul, i am 2 years old"
# x=txt.split(",")
# print(x)


# txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
# x = txt.split("#", 1)
#
# print(x)

#---------------------------------------------------------------------------------------------------

# join method - works with str only not with int

# myTuple = ("John", "Peter", "Vicky")
# mylist = ["John", "Peter", "Vicky"]

# x = "#".join(myTuple)
# x = " sherdil ".join(mylist)
#
# print(x)


# create an array of numbers
# numbers=[1,2,3,4,5]
# numbersline = '3'.join(numbers)
# print(numbersline)

#---------------------------------------------------------------------------------------------------

# String Insertion - works with both str and int

# list1 = [1,2,3,4,5,6,7]
# list1.insert(4,10)
# print(list1)

# list2= ['a','b','c','d','e']
# list2.insert(3,'z')
# print(list2)

# we can insert a list inside a list
# list2= ['a','b','c','d','e']
# list1 = [1,2,3,4,5,6,7]
# list2.insert(3,list1)
# print(list2)


# works with list not with strings
# 'str' object has no attribute 'insert'
# string="1234567"
# string.insert(10,1)
# print(string)