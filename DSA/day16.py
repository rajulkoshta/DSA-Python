
# https://leetcode.com/problems/lru-cache/submissions/

# class Dll():
#     def __init__(self , val=0 , key=0):
#         self.key = key
#         self.val= val
#         self.left = self.right = None
        
# def delete(node):
#     node.right.left , node.left.right = node.left , node.right
    
# def insertxleftofy(x,y):
#     x.left , x.right = y.left , y
#     y.left = x.left.right = x

# class LRUCache(object):

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.m = dict()
#         self.leftend , self.rightend = Dll() , Dll()
#         self.leftend.right , self.rightend.left = self.rightend , self.leftend
        

#     def get(self, key: int) -> int:
#         if key not in self.m:
#             return -1
#         node = self.m[key]
#         delete(node)
#         insertxleftofy(node,self.rightend)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.m:
#             node = self.m[key]
#             node.val=value
#             delete(node)
#         else:
#             node = Dll(value,key)
#             self.m[key] = node
#         insertxleftofy(node,self.rightend)
#         if len(self.m) > self.capacity:
#             k = self.leftend.right.key
#             delete(self.leftend.right) 
#             del self.m[k]  


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#============================================================================================
# https://leetcode.com/problems/all-oone-data-structure/

# class Dll():
#     def __init__(self , val=0 , key=0):
#         self.key = key
#         self.val= val
#         self.left = self.right = None
        
# def delete(node):
#     node.right.left , node.left.right = node.left , node.right
    
# def insertxleftofy(x,y):
#     x.left , x.right = y.left , y
#     y.left = x.left.right = x

# class AllOne(object):

#     def __init__(self):
#         self.m = dict()
#         self.leftend , self.rightend = Dll(-1,""),Dll(1000000,"")
#         self.leftend.right ,self.rightend.left = self.rightend , self.leftend

#     def inc(self, key: str) -> None:
#         if key not in self.m:
#             node = Dll(1,key)
#             insertxleftofy(node , self.leftend.right)
#             self.m[key] = node
#         else:
#             node = self.m[key]
#             node.val +=1
#             if node.val > node.right.val:
#                 n=node.right
#                 delete(node)
#                 while n.val<node.val:
#                     n = n.right
#                 insertxleftofy(node,n)

#     def dec(self, key: str) -> None:
#         node = self.m[key]
#         if node.val == 1:
#             delete(node)
#             del self.m[key]
#         else:
#             node.val-=1
#             if node.val < node.left.val:
#                 n=node.left
#                 delete(node)
#                 while n.val>node.val:
#                     n=n.left
#                 insertxleftofy(node,n.right)

#     def getMaxKey(self) -> str:
#         return self.rightend.left.key

#     def getMinKey(self) -> str:
#         return self.leftend.right.key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


#============================================================================================
#     ------------  |      |        /\
#          |        |      |       /  \
#          |        |------|      /----\
#          |        |      |     /      \
#          |        |      |    /        \


# https://leetcode.com/problems/lfu-cache/



















#============================================================================================
# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         start = ListNode(0,head)
#         start.next = head
#         curr , prev = head , start
#         while curr:
#             if curr.next and curr.next.val < curr.val:
#                 #insertion
#                 while prev.next and prev.next.val < curr.next.val:
#                     prev = prev.next
                
#                 temp = prev.next
#                 prev.next = curr.next
#                 curr.next = curr.next.next
#                 prev.next.next = temp
#                 prev =start
#             else:
#                 curr =curr.next
#         return start.next       
                
            
            