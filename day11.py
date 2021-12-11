# https://leetcode.com/problems/next-greater-element-i/submissions/
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# https://leetcode.com/problems/implement-stack-using-queues/
# https://leetcode.com/problems/implement-queue-using-stacks/
# https://leetcode.com/problems/single-element-in-a-sorted-array/

#============================================================================================

# https://leetcode.com/problems/next-greater-element-i/submissions/

    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     st = [-1]
    #     m = {}
    #     for el in nums2[::-1]:
    #         while st[-1] != -1 and st[-1] < el:
    #             st.pop()
    #         m[el]= st[-1]    
    #         st.append(el)    
    #     return [m[x] for x in nums1]   

#============================================================================================

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

    # def removeDuplicates(self, s: str) -> str:
    #     st = []
    #     for c in s:
    #         if st and st[-1] == c:
    #             st.pop()
    #         else:
    #             st.append(c)
    #     return "".join(st)

#============================================================================================



#---------------------------------------- THA ------------------------------------------------------


# https://leetcode.com/problems/implement-queue-using-stacks/

#-------------------------pop(n) push(1) ----------------------------
# class MyQueue:
#         self.s1=[]

#     def __init__(self):
#         self.s2=[]

#     def push(self, x: int) -> None:
#         self.s1.append(x)

#     def pop(self) -> int:
#         while len(self.s1)>0:
#             self.s2.append(self.s1.pop())
#         res = self.s2.pop()
#         while len(self.s2) > 0:
#             self.s1.append(self.s2.pop())
#         return res
        

#     def peek(self) -> int:
#         if self.s1:
#             return self.s1[0]

#     def empty(self) -> bool:
#         if self.s1:
#             return False
#         return True
#--------------------- pop(1) push(n)----------------------------
# class MyQueue:

#     def __init__(self):
#         self.s1=[]
#         self.s2=[]

#     def push(self, x: int) -> None:
#         while len(self.s2)>0:
#             self.s1.append(self.s2.pop())
#         self.s1.append(x)
#         while len(self.s1)>0:
#             self.s2.append(self.s1.pop())
            
#     def pop(self) -> int:
#         res = self.s2.pop()
#         return res
        
#     def peek(self) -> int:
#         if self.s2:
#             return self.s2[len(self.s2)-1]

#     def empty(self) -> bool:
#         if self.s2:
#             return False
#         return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


#============================================================================================

# https://leetcode.com/problems/implement-stack-using-queues/

#--------------------- pop(1) push(n)----------------------------
# from collections import deque

# class MyStack:

#     def __init__(self):
#         self.q1=deque()  
#         self.q2=deque()  

#     def push(self, x: int) -> None:
#         self.q2.append(x)
        
#         while len(self.q1) != 0:
#             self.q2.append(self.q1.popleft())
            
#         self.q1 , self.q2 = self.q2 , self.q1
        

#     def pop(self) -> int:          
#         return self.q1.popleft()

#     def top(self) -> int:       
#         return self.q1[0]
        
#     def empty(self) -> bool:
#         if len(self.q1):
#             return False
#         return True


#-------------------------pop(n) push(1) ----------------------------
    def __init__(self):
        self.q1=deque()  
        self.q2=deque()  

    def push(self, x: int) -> None:
        self.q1.append(x)        

    def pop(self) -> int:          
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res=self.q1.popleft()
        self.q1 , self.q2 = self.q2 , self.q1
        return res
    
    def top(self) -> int:       
        return self.q1[len(self.q1)-1]
        
    def empty(self) -> bool:
        if len(self.q1):
            return False
        return True




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


#============================================================================================

# https://leetcode.com/problems/single-element-in-a-sorted-array/


































#============================================================================================





















