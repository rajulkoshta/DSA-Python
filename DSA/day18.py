# Day 18:
#     What is a tree : as an extension of linked lists
#     root, parent , children
#     what is not a tree : every child has single parent
#     what is a binary tree
#     levels in a tree, leaf nodes, inner nodes
#     types of BT:
#         pefect: all levels completely filled
#             number of node
#             LN = IN +1
#         full: no parent has 1 child. 0 or 2.
#             LN = IN + 1
#             perfect bt is full bt
#         complete : all levels filled except last. last level filled left most.
#     traversals:
#         inorder
#         preorder
#         postorder
#         levelorder

#     THA:
#         implement all traversals


from collections import deque
class Node:
    def __init__(self,data=0,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1,
            Node(2,Node(4),Node(5)),
            Node(3,Node(6),Node(7)))

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data , end=" ")
        InOrder(root.right)


def PreOrder(root):
    if root:
        print(root.data , end=" ")
        InOrder(root.left)
        InOrder(root.right)

def PostOrder(root):
    if root:
        InOrder(root.left)
        InOrder(root.right)
        print(root.data , end=" ")
 
 # is wale code me pata nahi chal raha hai ki kon sa node kon se level par hai 

def LevelOrder1(root):
    q=deque([root]) 
    while len(q):
        node = q.pop()
        print(node.data, end = " ")
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)

# is code me separate ho pa rhae hai levels

def LevelOrder2(root):
    q=deque([None,root])

    while True:
        node = q.pop()
        if not node:
            if len(q)<1:
                return
            print("")
            q.appendleft(None)
            continue

        print(node.data , end =" ")
        
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right)

# level order representing is code me list of list ke form me represent kar sakte hai 
# https://leetcode.com/problems/binary-tree-level-order-traversal/
def LevelOrder3(root):
    q=deque([None,root])
    ans =[]
    curr = []
    while True:
        node = q.pop()
        if not node:
            if len(q)<1:
                ans.append(curr)
                print(ans)
                return
            ans.append(curr)
            curr=[]
            q.appendleft(None)
            continue

        curr.append(node.data)
        
        if node.left:
            q.appendleft(node.left)
        if node.right:
            q.appendleft(node.right) 

print("\nInOrder: ")
InOrder(root)
print("\nPreOrder: ")
PreOrder(root)
print("\nPostOrder: ")
PostOrder(root)
print("\nLevelOrder1: ")
LevelOrder1(root)
print("\nLevelOrder2: ")
LevelOrder2(root)
print("\nLevelOrder3: ")
LevelOrder3(root)