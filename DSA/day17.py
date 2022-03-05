# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# def make_equal_length(l1,l2):
#     k1,k2 = l1,l2
#     while k1 or k2:
#         (k1,l1) = (k1.next,l1) if k1 else (k1 , ListNode(0,l1))
#         (k2,l2) = (k2.next,l2) if k2 else (k2 , ListNode(0,l2))
#     return l1,l2

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         if not (l1.val and l2.val):
#             return l2 if l2.val else l1
#         l1, l2 = make_equal_length(l1,l2)
#         any_l2 = True
#         while any_l2:
#             l1_p , l2_p , prev , any_l2 = l1, l2, None, False
#             while l1_p:
#                 l1_p.val , l2_p.val = (l1_p.val+l2_p.val)%10, (l1_p.val+l2_p.val)//10
#                 any_l2 = any_l2 or l2_p.val
#                 l1_p , l2_p , prev = l1_p.next , l2_p.next ,l2_p
#             prev.next = ListNode(0)
#             (l1,l2) = (ListNode(0,l1),l2) if l2.val else (l1,l2.next)
#         print(l1)            
#         print(l2)
#         return l1
                
#============================================================================================

# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
#         head = p = ListNode(0,head)
#         l = r = head.next
#         while r:
#             if r.val == l.val:
#                 r = r.next
#             elif l.next is r:
#                 p.next = l
#                 p=p.next
#                 l=r
#             else:
#                 l=r
#         p.next = None if l.next else l
#         return head.next

#============================================================================================

# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         m={}
#         p = headA
#         while p:
#             m[id(p)] = p 
#             p=p.next
#         p=headB
#         while p:
#             if id(p) in m:
#                 return p
#             p=p.next
#         return None

#============================================================================================

# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow_p = fast_p = head
#         while fast_p and fast_p.next:
#             fast_p = fast_p.next.next
#             slow_p = slow_p.next
#             if slow_p == fast_p:
#                 fast_p = head
#                 while fast_p != slow_p:
#                     fast_p = fast_p.next
#                     slow_p = slow_p.next
#                 return slow_p
#         return None

#============================================================================================
#     ------------  |      |        /\
#          |        |      |       /  \
#          |        |------|      /----\
#          |        |      |     /      \
#          |        |      |    /        \

# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         f = s = head
#         while f and f.next:
#             f=f.next.next
#             s=s.next
#         return s
            

#============================================================================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         less = ListNode()
#         more = ListNode()
#         ltail,mtail = less,more
#         while head:
#             if head.val < x:
#                 ltail.next = head
#                 ltail = ltail.next
#             else:
#                 mtail.next = head
#                 mtail = mtail.next
#             head = head.next
#         ltail.next = more.next
#         mtail.next = None
#         return less.next   


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None
    
# class MyLinkedList:

#     def __init__(self):
#         self.length = 0
#         self.dummy = ListNode(0)

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.length:
#             return -1
#         curr = self.dummy.next
#         for _ in range(index):
#             curr = curr.next
#         return curr.val
        
#     def addAtHead(self, val: int) -> None:
#         curr = self.dummy.next
#         self.dummy.next = ListNode(val)
#         self.dummy.next.next = curr
#         self.length +=1

#     def addAtTail(self, val: int) -> None:
#         curr =self.dummy
#         while curr.next:
#             curr = curr.next
#         curr.next = ListNode(val)
#         self.length +=1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index >self.length:
#             return 
#         curr = self.dummy
#         for _ in range(index):
#             curr = curr.next
#         temp = curr.next
#         curr.next = ListNode(val)
#         curr.next.next = temp
#         self.length +=1
        

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.length:
#             return 
#         curr = self.dummy
#         for _ in range(index):
#             curr = curr.next
#         temp = curr.next
#         curr.next = temp.next
#         self.length -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)