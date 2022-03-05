# day 4:
#     hashing : hash(t)
#     hashmap and hashset
#     tuple: (1,2)
#     collections:
#         List is a collection which is ordered and changeable. Allows duplicate members.
#         Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#         Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#         Dictionary is a collection which is ordered** and changeable. No duplicate members.
#     https://www.hackerrank.com/challenges/python-tuples/problem
            # sol:
            # if __name__ == '__main__':
            #     n = int(raw_input())
            #     integer_list = map(int, raw_input().split())
            #     print(hash(tuple(integer_list)))

#     Recursion


#     THA:
#     https://www.hackerrank.com/challenges/finding-the-percentage/problem
#     https://www.hackerrank.com/challenges/triangle-quest-2/problem
#     https://www.hackerrank.com/challenges/python-mod-divmod/problem
#     https://www.hackerrank.com/challenges/word-order/problem

######################################################################################################################

# finding-the-percentage

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     marks = student_marks[query_name]
#     print("{0:.2f}".format(sum(marks)/len(marks)))

######################################################################################################################

# triangle-quest-2

# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print(((10**i-1)//9)**2)

######################################################################################################################

# python-mod-divmod

# a = int(input())
# b = int(input())
# tuple1 = divmod(a,b)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1)

######################################################################################################################

# word-order

# words = dict()
# for _ in range(int(input())):
#     word= input()
#     # print(word)     #just for checking purpose
#     words.setdefault(word,0)
#     words[word]+=1
#     # print(words)    #just for checking purpose
# print(len(words))
# print(*words.values())   