
# Syntax of Dictionary get()

# dict.get(key[, value]) 

# key - key to be searched in the dictionary
# value (optional) - Value to be returned if the key is not found. The default value is None.

# The get() method returns the value for the specified key if the key is in the dictionary.
#-----------------------------------------------
# Example:

# s="asdfghasdfghjkljkl"
# m={}
# for c in s:
#         m[c] = m.get(c,0)+1
# print(m)    # {'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2}
#----------------------------------------
# previously without get():

# s="asdfghasdfghjkljkl"
# m={}
# for c in s:
#   if c in m:
#         m[c]+=1
#   else:
#         m[c]=1
# print(m)  #{'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2}


#****************************************************************************************************
# day 13:
#     https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
#     https://leetcode.com/problems/remove-duplicate-letters/
#     https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/
#     https://www.geeksforgeeks.org/program-page-replacement-algorithms-set-2-fifo/
    
#     THA:
#     https://leetcode.com/problems/min-stack/
#         (Read : https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/)
#     https://www.geeksforgeeks.org/reversing-a-queue/
#     https://www.geeksforgeeks.org/reversing-first-k-elements-queue/
#     https://www.geeksforgeeks.org/sorting-queue-without-extra-space/

#============================================================================================

# day 13:
#     https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         n = len(prices)
#         st = [0]
#         nsee = [0]*n
#         for i in range(n-1,-1,-1):
#             while st[-1] != 0 and prices[i] < st[-1]:
#                 st.pop()
#             nsee[i] = st[-1]
#             st.append(prices[i])
#         return [x-y for x,y in zip(prices,nsee)] 


#============================================================================================
#     https://leetcode.com/problems/remove-duplicate-letters/



# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         last = {}
#         for i,e in enumerate(s):
#             last[e] = i
#         st = []
#         done= set()   
#         for i,e in enumerate(s):
#             if e not in done:
#                 while st and st[-1] > e and last[st[-1]] > i:   # LAST OCCURENCE 
#                     done.remove(st.pop())
#                 st.append(e)
#                 done.add(e)
#         return "".join(st) 


#============================================================================================
#     https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

# from collections import deque
# def binaryTill(n):
#     q=deque()
#     q.append("1")
#     while n:
#         el = q.popleft()
#         print(el)
#         n-=1
#         q.append(el+"0")
#         q.append(el+"1")
#     return q

# binaryTill(7)    


#============================================================================================
#     https://www.geeksforgeeks.org/program-page-replacement-algorithms-set-2-fifo/

# from collections import deque
# def pageFaults(pages , capacity):
#     s = set()
#     q = deque()
#     n = len(pages)
#     page_faults = 0
#     for page in pages:
#         if page in s:
#             print("page- Hit!")
#         elif len(s) == capacity:
#             el = q.popleft()
#             q.remove(el)
#         q.append(page)
#         s.add(page)
#         page_faults += 1
#     return page_faults 

# pageFaults()                


#============================================================================================

#     THA:
#     https://leetcode.com/problems/min-stack/
#         (Read : https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/)

# class MinStack:

#     def __init__(self):
#         self.st=[]
#         self.min = float("inf")
        
#     def push(self, val: int) -> None:
#         if val <= self.min:
#             self.st.append(self.min)
#             self.min = val
#         self.st.append(val)    
        

#     def pop(self) -> None:
#         top = self.st.pop()
#         if top == self.min:
#             self.min = self.st[-1]
#             self.st.pop()

#     def top(self) -> int:
#         return self.st[-1]

#     def getMin(self) -> int:
#         return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

















#============================================================================================
#     https://www.geeksforgeeks.org/reversing-a-queue/

# from queue import Queue

# def Print(queue):
#     while not queue.empty():
#         print(queue.queue[0] , end=" ")    
#         queue.get()

# def reversequue(queue):
#     st = []
#     while not queue.empty():
#         st.append(queue.queue[0])
#         queue.get()

#     while len(st)!=0:
#         queue.put(st[-1])
#         st.pop()

#     return queue

# if __name__ == "__main__":
#     queue = Queue()
#     queue.put(10)
#     queue.put(11)
#     queue.put(15)
#     queue.put(9)
#     queue.put(8)
#     queue.put(12)
#     queue.put(19)
#     queue.put(13)
#     queue.put(1)
#     # Print(queue)
#     reversequue(queue)
#     Print(queue)

#-------------------------------------------------------
# def solve(q):
#     st = []
#     for i in range(len(q)):
#         st.append(q.pop(0))
#     while len(st) != 0 :
#         el = st.pop()     
#         q.append(el)
#     return q    

# print(solve([1,2,3,4,5]))






#============================================================================================

#     https://www.geeksforgeeks.org/reversing-first-k-elements-queue/


# from queue import Queue

# def Print(queue):
#     while not queue.empty():
#         print(queue.queue[0] , end=" ")    
#         queue.get()

# def reverseKelements(q1,k):
#     st = []
#     for _ in range(k):
#         st.append(q1.queue[0])
#         q1.get()

#     while len(st) != 0:
#         q1.put(st[-1])
#         st.pop()

#     for _ in range(q1.qsize() - k):
#         q1.put(q1.queue[0])
#         q1.get()        

# if __name__ == "__main__":
#     q1 = Queue()
#     q1.put(10)
#     q1.put(20)
#     q1.put(30)
#     q1.put(40)
#     q1.put(50)
#     q1.put(60)
#     q1.put(70)
#     q1.put(80)
#     q1.put(90)
#     q1.put(100)
#     # Print(q1)
#     reverseKelements(q1,5)
#     Print(q1)

#---------------------------------------------

# using queue a list :

# def reverseKitems(q , k):
#     st = []
#     for _ in range(k):
#         front = q.pop(0)
#         st.append(front)
    
#     while len(st) != 0:
#         q.append(st[-1])
#         st.pop()

#     for _ in range(len(q)-k):
#         front = q.pop(0)
#         q.append(front)

#     return q    
    
# print(reverseKitems([10,20,30,40,50,60,70,80,90,100],5))







#============================================================================================
#     https://www.geeksforgeeks.org/sorting-queue-without-extra-space/

# def sort_queue(q):
#     for i in range(len(q)):
#         min_index = -1
#         min_value = float('inf')

#         for j in range(len(q)):
#             curr = q.pop(0)
#             if curr <=min_value and j <= (len(q)-i):
#                 min_value = curr
#                 min_index = j
#             q.append(curr)

#         for j in range(len(q)):
#             curr = q.pop(0)
#             if j!=min_index:
#                 q.append(curr)
#             else:
#                 min_value = curr 
#         q.append(min_value)
#     return q     

# print(sort_queue([12,11,21,4,6,7]))          

#-------------------------------------------------------------------------
# from queue import Queue

# def Print(queue):
#     while not queue.empty():
#         print(queue.queue[0] , end=" ")    
#         queue.get()

# def sort_queue(q):
#     n = q.qsize()
#     for i in range(n+1):
#         min_index = -1
#         min_value = float('inf')
#         for j in range(n):
#             curr = q.queue[0]
#             q.get()
#             if curr <= min_value and j <= (n-i):
#                 min_value = curr
#                 min_index = j
#             q.put(curr)

#         for j in range(n):
#             curr = q.queue[0]
#             q.get()
#             if j != min_index:
#                 q.put(curr)
#             else:
#                 min_value = curr 
#         q.put(min_value)
#     return q     

# if __name__ == "__main__":
#     q1 = Queue()
#     q1.put(11)
#     q1.put(21)
#     q1.put(4)
#     q1.put(7)
#     sort_queue(q1)
#     Print(q1)

#===========================================================================================