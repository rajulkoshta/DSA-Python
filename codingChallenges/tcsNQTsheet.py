# from numpy import array
# from itertools import count
# import sys

#?=====================================================

#! find the smallest element in array

#todo- sorting  o(nlogn)
# arr = [1,2,3,4,5,91,22,6]
# arr.sort()
# print(arr[0]) #1


#todo- min variable o(n)
# arr = [9,1,5,0,2,8,3,7]
# min = arr[0]
# for i in range(len(arr)):
#     if arr[i]<min:
#         min  = arr[i]
# print(min)

#?=====================================================


#! find the largest element in array

#todo-sorting 
# arr = [1,2,3,4,5,91,22,6]
# arr.sort()
# print(arr[len(arr)-1]) #1

#todo- max variable
# arr = [9,1,5,0,21,8,3,7]
# max = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
# print(max)
#?=====================================================

#! second largest and second smallest

#todo- sorting (nlogn)

# arr = [1,2,3,4,5,91,22,6]
# arr.sort()
# print(arr[1])
# print(arr[len(arr)-2])

#todo- double pass o(n)

# arr = [9,1,5,0,21,8,3,7]
# sec_max = -sys.maxsize-1
# sec_min = sys.maxsize 
# maxi =-sys.maxsize-1 
# mini = sys.maxsize 

# for i in range(len(arr)):
#     maxi = max(maxi,arr[i])
#     mini = min(mini,arr[i])

# for i in range(len(arr)):
#     if arr[i] > sec_max and arr[i] != maxi:
#         sec_max = arr[i]
#     if arr[i] < sec_min and arr[i] != mini:
#         sec_min = arr[i]

# print(sec_max)
# print(sec_min)

#todo- single pass o(n)

# def secondmaximum(arr,n):
#     maxi = sec_max = -sys.maxsize-1
#     for i in range(len(arr)):
#         if arr[i] > maxi:
#             sec_max = maxi
#             maxi = arr[i]
      
#         if arr[i] > sec_max and arr[i] != maxi:
#             sec_max = arr[i]
    
#     return sec_max

# def secondMinimum(arr,n):
#     mini = sec_min = sys.maxsize 
#     for i in range(len(arr)):

#         if arr[i] < mini:
#             sec_min = mini
#             mini = arr[i]

#         if arr[i] < sec_min and arr[i] != mini:
#             sec_min = arr[i]
    
#     return sec_min

# arr = [9,1,5,0,21,8,3,7]
# n=len(arr)
# secondmax = secondmaximum(arr,n)
# secondmmin = secondMinimum(arr,n)
# print(secondmax)
# print(secondmmin)

#?=====================================================

#! reverse the list or array

#todo- using extra array
# arr = [9,1,5,8,3,7]
# n=len(arr)
# rev_arr = []*n
# for i in range(n):
#     rev_arr.append(arr[n-1-i])
# print(rev_arr)

#todo- using swap in the same array(in space)
# arr = [9,1,5,8,3,7]
# n=len(arr)
# for i in range(n//2):
#     arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
# print(arr)

#todo- recursive

# def rec(arr,start,end):
#     if start < end:
#         arr[start],arr[end] = arr[end] , arr[start]    
#         return rec(arr,start+1 , end-1)

# arr = [9,1,5,8,3,7]
# n=len(arr)
# rec(arr,0,n-1)
# print(arr)

#?=====================================================

#! frequency count 

#todo- using extra array
# arr = [10,5,10,15,10,5]
# n =len(arr)
# visited=[False]*n     
# for i in range(n-1):
#     if visited[i] == True:
#        continue
#     count = 1
#     for j in range(i+1,n):
#         if arr[i]==arr[j]:
#             visited[j] = True
#             count+=1
#     print(f"{arr[i]} {count}")    


#todo- dictionary or map

# arr = [10,5,10,15,10,5]
# n =len(arr)
# map = {}
# for i in range(0,n-1):
#     if arr[i] in map.keys():
#         map.setdefault(arr[i],map.get(arr[i])+1)
#     else:
#         map.setdefault(arr[i],1)      
# print(map)

#?=====================================================

#! Rearrange array in increasing-decreasing order

# todo - intution
# arr = [8,7,1,6,5,9]
# n = len(arr)
# arr.sort()
# for i in range(0,n//2):
#     print(arr[i],end=" ")
# for i in range(n):
#     if i < n//2:
#         print(arr[n-1-i],end=" ")

#?=====================================================

#! sum of all elemnets of list

#todo- using built in 
# arr = [8,7,1,6,5,9]
# n = len(arr)
# print(sum(arr))

#todo - using sum variable  
# arr = [8,7,1,6,5,9]
# n = len(arr)
# sum  = 0
# for i in range(n):
#     sum += arr[i]
# print(sum)

#?=====================================================

#! Rotate array by K elements : time    space
# brute force                   o(n*r)  o(1)
# using temporary variable      o(n*r)  o(1)
# using auxillary array         o(n)    o(n)
# juggling algorithm            o(n)    o(1)
# reversal algorithm            o(n)    o(1)
# Block Swap Algorithm          o(n)    o(1)

# todo - brute force

# arr = [1,2,3,4,5]
# n = len(arr)
# k=2
# for _ in range(0,k):
#     el = arr.pop(0)
#     arr.append(el)
# print(arr)

# todo - auxillary array
# arr = [1,2,3,4,5]
# n = len(arr)
# k=2
# arr_aux = []*k
# for _ in range(k):
#     arr_aux.append(arr.pop(0))
# for _ in range(k):
#     arr.append(arr_aux.pop(0)) 
# print(arr)

#todo using temporary variable 

# def rotate(arr,n):
#     temp = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp

# arr = [1,2,3,4,5]
# n = len(arr)
# k=2
# for i in range(k):
#     rotate(arr,n)
# print(arr)

#todo juggling algorithm   - need attention


#todo -  Block Swap Algorithm - iterative

# def swap(arr,start,end,k):
#     for i in range(k):
#         arr[start+i],arr[end+i] = arr[end+i],arr[start+i]


# def rotate(arr, k ,n):
#     if k==0 or k==n:
#         return
#     i = k
#     j = n-k
#     while i!=j:
#         if i<j: #* A is shorter
#             swap(arr,k-i,k+j-i,i)
#             j=j-i
#         else:
#             swap(arr,k-i,k,j)
#             i=i-j
#     swap(arr,k-i,k,j)


# arr = [1,2,3,4,5]
# n = len(arr)
# k = 2
# rotate(arr,k,n)
# print(arr)

#todo -  Block Swap Algorithm - Recursive  -- need attention


#?=====================================================

#! Average of all the elements in the array


#todo -  using inbuilt "sum"

# arr = [1,2,3,4,5]
# n = len(arr) 
# s = sum(arr) 
# avg = s//n
# print(avg)

#todo - without using sum

# arr = [1,2,3,4,5]
# n = len(arr) 
# sum = 0
# for i in range(n):
#     sum+=arr[i] 
# avg = sum//n
# print(avg)

#?=====================================================

#! Find the median of the given array

#todo  - intution -- Time Complexity: O(N*log N), Sorting of array

# arr = [4,7,1,2,5]
# n = len(arr) 
# arr.sort(  )
# print(arr)
# if n%2 == 0:
#     median = float((arr[int((n-1)/2)] +
#                   arr[int(n/2)])/2.0)
# else:
#     median = float(arr[int(n/2)])
# print(median)


#?=====================================================

#! Remove duplicates from a sorted array

#todo  - using set  (time ccomplexity :  O(n*log(n))+O(n) )

# arr = [1,1,1,1,2,2,2,3,3,3]
# n = len(arr)
# arr = set(arr)
# s = list(arr)
# print(s)
# print(len(s))


#todo --> Two pointer (time complexity: O(n))

# arr = [1,1,1,1,2,2,2,3,3,3]
# n = len(arr)
# i=0
# j=1
# for j in range(n):
#     if arr[j] != arr[i]:
#         i+=1
#         arr[i] = arr[j]

# print(i+1) 



#?=====================================================

#! Remove duplicates from a unsorted array
#todo  - intution using a mark array and two pointer O(n*n) + O(n) 

# arr = [1,8,3,7,2,3,1,6,8,6,7]
# print(set(arr))
# n = len(arr)
# mark = [True]*n
# for i in range(n-1):
#     if mark[i] == True:
#         for j in range(i+1,n):
#             if arr[i] == arr[j]:
#                 mark[j] = False

# for i in range(n-1):
#     if mark[i] == True:
#         print(arr[i],end=" ")    

#todo  - using hashmap | Time Complexity: O(n) + O(n) = O(n) | Reason : Iteration in array , searching hash table | Space Complexity : O(n) 

# from operator import contains


# arr = [4, 3, 9, 2, 4, 1, 10, 89, 34]
# n = len(arr)

# map = {}

# for i in range(n-1):
#     if not arr[i] in map.keys():
#         print(arr[i],end=" ")
#         map[arr[i]] = 1    

#?=====================================================
#! Adding Element in an Array
#todo  - 

# def insert_at_begining(arr,n,value):
#     for i in range(n-1,-1,-1):
#         arr[i+1] = arr[i]
#     arr[0] = value    
# def insert_at_end(arr,n,value):
#     arr[n-1] = value
# def insert_at_specific(arr,n,val,index):
#     for i in range(index,n-1):
#         arr[i+1] = arr[i]
#     arr[index] = val

# n = 6
# arr = [10,9,14,23,21]*n
# insert_at_begining(arr,n,value)
# insert_at_end(arr,n,40)
# insert_at_specific(arr,n,40,3)
# for i in range(n):
#     print(arr[i],end=" ")


#?=====================================================

#! reapting elements in an array 
#todo  - using mark array o(n*n) + o(n)

# arr = [10,9,1,14,1,23,2,21,2]
# n = len(arr)
# mark = [True]*n

# for i in range(n-1):
#     if mark[i] == True:
#         for j in range(i+1,n):
#             if arr[i] == arr[j]:
#                 mark[j]=False
# print(mark)
# for i in range(n):
#     if mark[i] == False:
#         print(arr[i],end=" ")


#todo  -  using auxillary array o(n*n) + o(n)

# arr = [1,9,1,3,14,3,1,2,21,2]
# n = len(arr)
# dup = [0]*n
# count = 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             dup[count] = arr[i]
#             count+=1

# for i in range(count):
#     if dup[i] != dup[i+1] :
#         print(dup[i],end=" ")

#todo - sorting

# arr = [1,9,1,3,14,3,1,2,21,2]
# n = len(arr)
# arr.sort()
# print(arr)
# for i in range(n-1):
#     if arr[i] == arr[i+1]:
#         print(arr[i] ,end=" ")

#todo - hashmaps

# arr = [1,9,1,3,14,3,1,2,21,2]
# n = len(arr)
# map = {}
# for i in arr:
#     if i not in map:
#         map[i] = 1 
#     else:
#         map[i] = map[i] + 1    
# for key,val in map.items():
#     if val > 1:
#         print(key,end=" ")
# print(map)       


#?=====================================================

#! non reapting
#todo  - hashmap / dictionary
# arr = [1,2,-1,1,3,1]
# n = len(arr)
# map = {}
# for i in arr:
#     if i not in map:
#         map[i] = 1 
#     else:
#         map[i] = map[i] + 1    
# for key,val in map.items():
#     if val == 1:
#         print(key,end=" ")
 

#todo  - brute force
# arr = [1,2,-1,1,3,1]
# n = len(arr)
# for i in range(n-1):
#     chk = False
#     for j in range(n-1):
#         if i != j and arr[i] == arr[j]:
#             chk = True
#             break
#     if not chk:
        # print(arr[i],end=" ")
    
#todo - sorting

# arr  = [1,2,-1,1,3,1]
# arr.sort()
# n = len(arr)
# if arr[0] != arr[1]:
#     print(arr[0],end=" ")

# for i in range(1,n-1):
#     if arr[i-1]!=arr[i] and arr[i]!=arr[i+1]:
#         print(arr[i],end=" ")

# if arr[n-2] != arr[n-1]:
#     print(arr[n-1])



#?=====================================================

#! Find all Symmetric Pairs in the array of pairs
#todo  - brute force

# arr = [[1,2],[2,1],[2,1],[4,5],[5,4]]
# n = len(arr)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[j][1] == arr[i][0] and arr[j][0]==arr[i][1]:
#             print(f"({arr[i][0]},{arr[i][1]})")
#             break


#todo  - dictionary

# arr = [[1,2],[2,1],[3,4],[3,2],[4,5],[5,4],[2,3]]
# n = len(arr)
# map={}

# for i in range(n):
#     first = arr[i][0]
#     second = arr[i][1]

#     if map.get(second) != None and map.get(second) == first :
#         print(f"({second},{first})" , end=" ")
#     else:
#         map[first] = second   

#?=====================================================

#! maximum product subarray
#todo  -  brute force

arr = [1,2,-3,0,-4,-5]
n = len(arr)

for i in range(n-1):
    prod = arr[i]
    for j in range(i+1,n-1):
        prod *= arr[j]
    


#?=====================================================

#!
#todo  - 

#?=====================================================

#!
#todo  - 
#?=====================================================


#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================

#!
#todo  - 
#?=====================================================










