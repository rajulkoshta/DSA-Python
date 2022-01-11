# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#---------------------------------------------------using or
# class Solution:
#     def addTwoNumbers(self,l1, l2):
#         carry = 0
#         ans = p = ListNode()

#         while l1 or l2:
#             if not l2.next:
#                 l2.val = 0
#             if not l1.next:
#                 l1.val = 0
                
#             k = l1.val + l2.val + carry
#             p.next = ListNode(k%10)
#             p = p.next
#             carry = k//10
            
#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next
      
#         if carry:
#             p.next = ListNode(carry)
            
#         return ans.next
       
    
#----------------------------------------------------------using  "" and ""    
        # while l1 and l2:
        #     k = l1.val + l2.val + carry
        #     p.next = ListNode(k%10)
        #     carry = k//10
        #     p,l1,l2 = p.next,l1.next,l2.next
        # if l2:
        #     l1 = l2
        # while l1:
        #     k = l1.val + carry
        #     p.next = ListNode(k%10)
        #     carry = k//10
        #     p,l1 =  p.next,l1.next
        # if carry:
        #     p.next = ListNode(carry)
        # return ans.next

#============================================================================================

# https://leetcode.com/problems/reorder-list/


# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#---------------------------------------------- normal array or list to linked list 
# def insert(root, item):
#     temp = ListNode(item)
     
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
#----------------------------------------- 
# def cutinhalf(head):
#     fast , slow = head.next , head
#     if not fast:
#         return None 
#     while fast.next and fast.next.next:
#         slow = slow.next
#         fast = fast.next.next
        
#     if fast.next:
#         slow= slow.next
#     x = slow.next
#     slow.next = None
#     return x

# def reverse(head):
#     if not head or not head.next:
#         return head
#     p,c,n = head,head.next,head.next.next
#     p.next = None
#     while n:
#         c.next=p
#         p = c
#         c=n
#         n=n.next
#     c.next = p
#     return c  

# #class Solution:
#     def reorderList(self, head):
#         h = cutinhalf(head)
#         h = reverse(h)
#         p = head
#         while h:
#             h2 = h.next
#             h.next = p.next
#             p.next = h
#             p,h = p.next.next , h2
#         return head

# # Driver code
# if __name__=='__main__':
#     arr1=[1,2,4,5,6,8]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.reorderList(l1)  
#============================================================================================

# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = ListNode(item)
     
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
#     def oddEvenList(self, head):
#         if not head or not head.next or not head.next.next:
#             return head
#         odd = head
#         even = head.next
        
#         while even and even.next:
#             x = even.next
#             even.next = even.next.next
#             x.next = odd.next
#             odd.next = x
#             even = even.next
#             odd = odd.next
#         return head


# #  Driver code
# if __name__=='__main__':
#     arr1=[1,2,4,5,6,8]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.oddEvenList(l1) 
#============================================================================================

# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = ListNode(item)
     
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
#     def swapPairs(self, head):
        
#         ## using recursion
#         # if not head or not head.next:
#         #     return head
#         # p=head.next.next
#         # head.next.next = head
#         # newhead = head.next
#         # head.next = self.swapPairs(p)
#         # return newhead
        
        
#         ##using iteration
#         dummy = ListNode(0 , head)
#         prev = dummy
#         curr = head
        
#         while curr and curr.next:
#             prev.next = curr.next
#             curr.next = curr.next.next
#             prev.next.next = curr
#             curr = curr.next
#             prev = prev.next.next
            
#         return dummy.next
        
# # #  Driver code
# if __name__=='__main__':
#     arr1=[1,2,4,5,6,8]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.swapPairs(l1)  


#============================================================================================
#     ------------  |      |        /\
#          |        |      |       /  \
#          |        |------|      /----\
#          |        |      |     /      \
#          |        |      |    /        \


# https://leetcode.com/problems/palindrome-linked-list/submissions/


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# def insert(root, item):
#     temp = ListNode(item)
     
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
#     def isPalindrome(self, head):
#         fast=head
#         slow=head
        
# # find  middle

#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
            
# # reverse the half part

#         prev = None
#         while slow:
#             temp = slow.next
#             slow.next = prev
#             prev = slow
#             slow= temp
            
# # check palindrome

#         left , right = head , prev
#         while right:
#             if left.val != right.val:
#                 return False
#             left = left.next
#             right = right.next
#         return True 
        
# # #  Driver code
# if __name__=='__main__':
#     arr1=[1,2,4,5,6,8]
#     n1 = len(arr1)
#     l1 = arrayToList(arr1, n1)
#     sol=Solution() 
#     sol.isPalindrome(l1)         

#-------------------------------------------------using Arrays
#         nums=[]
#         while head:
#             nums.append(head.val)
#             head = head.next
        
#         l ,r = 0 , len(nums)-1
#         while l<=r:
#             if nums[l] != nums[r]:
#                 return False
#             l+=1
#             r-=1
#         return True 

#============================================================================================

# https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         if not head:
#             return head
        
#         length, tail = 1 , head
#         while tail.next:
#             tail = tail.next
#             length +=1
#         k = k % length
#         if k==0:
#             return head
        
#         curr= head
#         for i in range(length - k - 1):
#             curr = curr.next
#         newhead = curr.next
#         curr.next = None
#         tail.next = head
        
#         return newhead


#============================================================================================
# https://leetcode.com/problems/reverse-linked-list-ii/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         if not head or left==right:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
        
#         prev_Before_Left = dummy
        
#         for _ in range(left-1):
#             prev_Before_Left= prev_Before_Left.next
        
#         reverse = None
#         curr = prev_Before_Left.next
#         for _ in range(right - left + 1):
#             next = curr.next
#             curr.next = reverse
#             reverse  = curr
#             curr = next
        
#         prev_Before_Left.next.next = curr
#         prev_Before_Left.next  = reverse
        
#         return dummy.next
    
#==========================================================================================
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         p1=p2=head
       
#         for _ in range(n):
#             p2 = p2.next
        
#         if not p2:
#             return head.next
        
#         while p2.next:
#             p2 = p2.next
#             p1 = p1.next
        
#         p1.next = p1.next.next
        
#         return head


#-----------------------------------recursion solution -- jo samajh hii niii aya
class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

#-----------------------------------
class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]        
        
#==========================================================================================
