# Day 3:
#     in keyword
#     functions
#     return values
#     default args
#     main()
#     scope
#     global
#     functions : passing string as s[:]
#     input()
#     split() join()
#     min() max()
#     list comprehensions() : if / if else
#     map()

# THA:
#     https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#     https://www.hackerrank.com/challenges/nested-list/problem
#     https://www.hackerrank.com/challenges/python-string-split-and-join/problem
#     https://www.hackerrank.com/challenges/designer-door-mat/problem

####################################################################################################
#     find-second-maximum-number-in-a-list

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(set(map(int, input().split())))
#     max_el=max(arr)
#     indexof = arr.index(max_el)
#     arr.pop(indexof)
#     now_max_el=max(arr)
#     print(now_max_el)

#-----------------------------------------------------------
# better approach

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     winner = arr[0]
#     runnerUp = -101
#     for i in range(1,n):
#         #print(wineer,runnerup)
#         if arr[i] > winner:
#             runnerUp = winner
#             winner = arr[i]
#         elif arr[i] > runnerUp and arr[i] != winner:
#             runnerUp = arr[i]
#     print(runnerUp)

##########################################################################################################

# nested-list


# if __name__ == '__main__':
#     marks_list = []
#     second_lowest_names = []
#     marks = set()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         marks_list.append([name, score])
#         marks.add(score)
# second_lowest_marks = sorted(marks)[1]

# # print(marks) # {41.0, 37.2, 37.21, 39.0}
# # print(second_lowest_marks)  # 37.21
# # print(marks_list)  #[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]

# for name, score in marks_list:
#     if score == second_lowest_marks:
#         second_lowest_names.append(name)

# for name in sorted(second_lowest_names):
#     print(name)
#--------------------------------------------------------------      
# better approach

# import sys
# if __name__ == '__main__':
#     nested = []
#     lowest = sys.maxsize
#     lowset2 = sys.maxsize

#     for _ in range(int(input())):
#          name = input()
#          score = float(input())
#          newList = [name,score]
#          nested.append(newList)

#          if score < lowest:
#              lowest2 = lowest
#              lowest = score

#          elif score < lowest2 and score != lowest:
#              lowest2 = score  
#     nameList = []
#     for l in nested:
#         if l[1] == lowest2:
#             nameList.append(l[0])
#     nameList.sort()
#     for naam in nameList:
#         print(naam)                     
##############################################################################################

# doormat
# 
# n,m = map(int,input().split())
# pattern=[]
# for i in range(n//2):
#     pattern.append((".|." * ( 2*i + 1)).center(m,"-"))
# print('\n'.join(pattern + ["WELCOME".center(m,"-")]+pattern[::-1])) 

########################################################################

# split and join

# def split_and_join(line):
#     line=line.split(" ")
#     line="-".join(line)
#     return line

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)
 