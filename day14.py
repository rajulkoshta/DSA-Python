#  Today is the most important day in DSA course. We will start Linked List. All topics here on out will be based on concepts of linked lists. Must-Attend if you can.

# Day14:
#     association of data
#     class
#     pass
#     objects
#     _init_
#     self
#     functions
#     dunder methods : _add_ , _len_ , _repr_

#     linked lists:
#         reason
#         base idea
#         implementation
#         vs array

#     example:
#         creation
#         print LL // counting (iterative / recursive)
#         insert at Last
#         insert at front
#         delete element at kth position

#     types: singly doubly circular

#     https://leetcode.com/problems/merge-two-sorted-lists/
#     https://leetcode.com/problems/reverse-linked-list/

#     THA:
#         if you want to go through more builtin methods (https://docs.python.org/3/reference/datamodel.html#special-method-names)
#         https://leetcode.com/problems/reverse-linked-list/ (do this recursively)
#         https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
#         https://leetcode.com/problems/delete-node-in-a-linked-list/



#-----------------------------------------------------------------------------------------------------

#     https://leetcode.com/problems/merge-two-sorted-lists/

# visulaizer
 
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = Node(item)
     
#     if (root == None):
#         root = temp
#     else :
#         ptr = root
#         while (ptr.next != None):
#             ptr = ptr.next
#         ptr.next = temp
     
#     return root
 
# def display(root):
#     while (root != None) :
#         print(root.data, end = " ")
#         root = root.next
         
# def arrayToList(arr, n):
#     root = None
#     for i in range(0, n, 1):
#         root = insert(root, arr[i])
     
#     return root
 
# leetcode Runable:

# class Solution:
#     def mergeTwoLists(self,l1, l2):
#         head = p = Node()
#         while l1 and l2:
#             if l1.val < l2.val:
#                 p.next = l1
#                 l1 = l1.next
#             else:
#                 p.next = l2
#                 l2 = l2.next
#             p=p.next
#         if l1:
#             p.next = l1
#         else:
#             p.next = l2
#         return head.next          

#         # Driver code
# if __name__=='__main__':
#     arr1,arr2=[1,2,4],[1,3,4]
#     n1,n2 = len(arr1),len(arr2)
#     l1,l2 = arrayToList(arr1, n1),arrayToList(arr2, n2)
#     sol=Solution() 
#     sol.mergeTwoLists(l1,l2)    

#---------------------------------------------------------------------------------------------------------
#     https://leetcode.com/problems/reverse-linked-list/

# visulaizer
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = Node(item)
     
#     if (root == None):
#         root = temp
#     else :
#         ptr = root
#         while (ptr.next != None):
#             ptr = ptr.next
#         ptr.next = temp
     
#     return root
 
# def display(root):
#     while (root != None) :
#         print(root.data, end = " ")
#         root = root.next
         
# def arrayToList(arr, n):
#     root = None
#     for i in range(0, n, 1):
#         root = insert(root, arr[i])
     
#     return root
 
#  leetcode runable:
#-------------------------
# class Solution:
#     def reverseList(self, head):
#         if not head or not head.next:
#             return head
#         p,c,n = head,head.next,head.next.next
#         p.next = None
#         while n:
#             c.next=p
#             p = c
#             c=n
#             n=n.next
#         c.next = p
#         return c
            


#         # Driver code
# if __name__=='__main__':
#     arr1=[1,2,4,5,6,8]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.reverseList(l1)   

#---------------------------------------------------------------------------------------------------------

    # ----------------------- THA---------------------------
# using recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:   
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         prev = None
#         def rec(head):
#             nonlocal prev
#             if head == None:
#                 return head
#             nex = head.next
#             head.next = prev
#             prev = head
#             head = nex
#             rec(head)
#         rec(head) 
# #---------------------------------------------------------------------------------------------------------

# # https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# # visulaizer
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = Node(item)
     
#     if (root == None):
#         root = temp
#     else :
#         ptr = root
#         while (ptr.next != None):
#             ptr = ptr.next
#         ptr.next = temp
     
#     return root
 
# def display(root):
#     while (root != None) :
#         print(root.data, end = " ")
#         root = root.next
         
# def arrayToList(arr, n):
#     root = None
#     for i in range(0, n, 1):
#         root = insert(root, arr[i])
     
#     return root
# class Solution:
#     def getDecimalValue(self, head) -> int:
#         num = head.val
#         while head.next:
#             num = num <<1 | head.next.val     # num = num *2 + head.next.value
#             head = head.next
#         return num
        
        
# # Driver code
# if __name__=='__main__':
#     arr1=[1,0,1,1,0,1,0,0,1]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.getDecimalValue(l1)

#---------------------------------------------------------------------------------------------------------
# https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def deleteNode(self, node):
#         """
#         :type node: ListNode
#         :rtype: void Do not return anything, modify node in-place instead.
#         """
#         node.val = node.next.val
#         node.next = node.next.next

 # USING WHILE LOOP -- not working right now
        # nex=node.next
        # while nex.next:
        #     node.val,nex.val = nex.val,node.val
        #     node = node.next
        #     nex = nex.next
        # node.val,nex.val = nex.val,node.val    
        # node.next = None 