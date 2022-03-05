# Day 19:
#     print leaf nodes
#     sum of all nodes
#     sum of all nodes which have even value

# things to remember:

# not root.left and not root.right ~~~ not (root.left or root.right)
# not root.left or not root.right ~~~ not (root.left and root.right)

# https://leetcode.com/problems/same-tree/
# https://leetcode.com/problems/invert-binary-tree/
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solution/

# THA:

# https://leetcode.com/problems/symmetric-tree/submissions/
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# class Node:
#     def __init__(self,data=0,left=None , right = None):
#         self.data = data
#         self.left = left
#         self.right = right

# root  =  Node(1,Node(2,Node(4),Node(5)),Node(3,Node(6),Node(7)))

# # print leaf nodes

# def print_all_leaf_node(root):
#     if root:
#         if not root.left and not root.right:
#             print(root.data,end=" ")
#         print_all_leaf_node(root.left)
#         print_all_leaf_node(root.right)

# # sum of all nodes can be performed using 
# # levelOrder traversal 
# # preorder root-L-R -> (topdown approach) not so optimized  
# # or postOrder L-R-root (bottom up approach)

# def sumAll(root):
#     if root:
#         return  root.data + sumAll(root.left) + sumAll(root.right)
#     return 0

# # sum of all nodes which have even value

# def sum_with_even_value(root):
#     if root:
#         return (root.data if not root.data%2 else 0) + sum_with_even_value(root.left) + sum_with_even_value(root.right)
#     return 0


# #  sum of all leaf nodes

# def sumLeaf(root):
#     if root:
#         if not (root.left or root.right):
#             return root.data
#         return sumLeaf(root.left) + sumLeaf(root.right)
#     return 0

# # Another way

# def sumLeaf1(root):
#     if not (root.left or root.right):
#         return root.data
#     sum= sumLeaf1(root.left) if root.left else 0
#     sum+=sumLeaf1(root.right) if root.right else 0
#     return sum 

# print(sum_with_even_value(root))
# print(sumAll(root))
# print(sumLeaf(root))  
# print(sumLeaf1(root))    
# print_all_leaf_node(root)


#============================================================================================


# LEETCODE CLASS Work:  : https://leetcode.com/problems/same-tree/
# Approach 1: Recursion
# Intuition

# The simplest strategy here is to use recursion. Check if p and q nodes are not None, and their values are equal. If all checks are OK, do the same for the child nodes recursively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if (p or q) and not(p and q):
#             return False
#         return (not p and not q) or ((p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

#  OR

# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """    
#         # p and q are both None
#         if not p and not q:
#             return True
#         # one of p and q is None
#         if not q or not p:
#             return False
#         if p.val != q.val:
#             return False
#         return self.isSameTree(p.right, q.right) and \
#                self.isSameTree(p.left, q.left)

# Complexity Analysis
# Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
# Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Approach 2: Iteration
# Intuition

# Start from the root and then at each iteration pop the current node out of the deque. Then do the same checks as in the approach 1 :

# p and p are not None,

# p.val is equal to q.val,

# and if checks are OK, push the child nodes.

# Implementation
# from collections import deque
# class Solution:
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """    
#         def check(p, q):
#             # if both are None
#             if not p and not q:
#                 return True
#             # one of p and q is None
#             if not q or not p:
#                 return False
#             if p.val != q.val:
#                 return False
#             return True
        
#         deq = deque([(p, q),])
#         while deq:
#             p, q = deq.popleft()
#             if not check(p, q):
#                 return False
            
#             if p:
#                 deq.append((p.left, q.left))
#                 deq.append((p.right, q.right))
                    
#         return True


# Complexity Analysis

# Time complexity : O(N) since each node is visited exactly once.

# Space complexity : O(log(N)) in the best case of completely balanced tree and O(N) in the worst case of completely unbalanced tree, to keep a deque.


#============================================================================================
# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root:
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#             # temp = root.left
#             # root.left = root.right
#             # root.right = temp
#             root.left , root.right = root.right,root.left
#         return root   

#============================================================================================
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/solution/

# Approach 1: Iterative Preorder Traversal.
# Intuition
# Here we implement standard iterative preorder traversal with the stack:
# Push root into stack.
# While stack is not empty:
# Pop out a node from stack and update the current number.
# If the node is a leaf, update root-to-leaf sum.
# Push right and left child nodes into stack.


# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         root_to_leaf = 0
#         stack = [(root, 0) ]
        
#         while stack:
#             root, curr_number = stack.pop()
#             if root is not None:
#                 curr_number = (curr_number << 1) | root.val
#                 # if it's a leaf, update root-to-leaf sum
#                 if root.left is None and root.right is None:
#                     root_to_leaf += curr_number
#                 else:
#                     stack.append((root.right, curr_number))
#                     stack.append((root.left, curr_number))
                        
#         return root_to_leaf

# Complexity Analysis

# Time complexity:O(N), where NN is a number of nodes, since one has to visit each node.

# Space complexity: up to O(H) to keep the stack, where HH is a tree height.

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Approach 2: Recursive Preorder Traversal.
# Iterative approach 1 could be converted into recursive one.

# Recursive preorder traversal is extremely simple: follow Root->Left->Right direction, i.e. do all the business with the node (= update the current number and root-to-leaf sum), and then do the recursive calls for the left and right child nodes.

# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         def preorder(r, curr_number):
#             nonlocal root_to_leaf
#             if r:
#                 curr_number = (curr_number << 1) | r.val
#                 # if it's a leaf, update root-to-leaf sum
#                 if not (r.left or r.right):
#                     root_to_leaf += curr_number
                    
#                 preorder(r.left, curr_number)
#                 preorder(r.right, curr_number) 
        
#         root_to_leaf = 0
#         preorder(root, 0)
#         return root_to_leaf

# OR

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def f(root,ans):
#     if root:
#         ans = (2*ans) + root.val
#         if not root.left and not root.right:
#             return ans
#         return f(root.left,ans) + f(root.right,ans)
#     return 0
# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         return f(root,0)


# Complexity Analysis

# Time complexity: O(N), where NN is a number of nodes, since one has to visit each node.
# Space complexity: up to O(H) to keep the recursion stack, where HH is a tree height.

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Approach 3: Morris Preorder Traversal.
# We discussed already iterative and recursive preorder traversals, which both have great time complexity though use up to O(H) to keep the stack. We could trade in performance to save space.
# The idea of Morris preorder traversal is simple: to use no space but to traverse the tree.
# How that could be even possible? At each node one has to decide where to go: to the left or to the right, traverse the left subtree or traverse the right subtree. How one could know that the left subtree is already done if no additional memory is allowed?
# The idea of Morris algorithm is to set the temporary link between the node and its predecessor: predecessor.right = root. So one starts from the node, computes its predecessor and verifies if the link is present.
# There is no link? Set it and go to the left subtree.
# There is a link? Break it and go to the right subtree.
# There is one small issue to deal with : what if there is no left child, i.e. there is no left subtree? Then go straightforward to the right subtree.

# class Solution:
#     def sumRootToLeaf(self, root: TreeNode) -> int:
#         root_to_leaf = curr_number = 0
        
#         while root:  
#             # If there is a left child,
#             # then compute the predecessor.
#             # If there is no link predecessor.right = root --> set it.
#             # If there is a link predecessor.right = root --> break it.
#             if root.left: 
#                 # Predecessor node is one step to the left 
#                 # and then to the right till you can.
#                 predecessor = root.left 
#                 steps = 1
#                 while predecessor.right and predecessor.right is not root: 
#                     predecessor = predecessor.right 
#                     steps += 1

#                 # Set link predecessor.right = root
#                 # and go to explore the left subtree
#                 if predecessor.right is None:
#                     curr_number = (curr_number << 1) | root.val                    
#                     predecessor.right = root  
#                     root = root.left  
#                 # Break the link predecessor.right = root
#                 # Once the link is broken, 
#                 # it's time to change subtree and go to the right
#                 else:
#                     # If you're on the leaf, update the sum
#                     if predecessor.left is None:
#                         root_to_leaf += curr_number
#                     # This part of tree is explored, backtrack
#                     for _ in range(steps):
#                         curr_number >>= 1
#                     predecessor.right = None
#                     root = root.right 
                    
#             # If there is no left child
#             # then just go right.        
#             else: 
#                 curr_number = (curr_number << 1) | root.val
#                 # if you're on the leaf, update the sum
#                 if root.right is None:
#                     root_to_leaf += curr_number
#                 root = root.right
                        
#         return root_to_leaf

# Complexity Analysis

# Time complexity: O(N), where NN is a number of nodes.
# Space complexity: O(1).

#============================================================================================
#     ------------  |      |        /\
#          |        |      |       /  \
#          |        |------|      /----\
#          |        |      |     /      \
#          |        |      |    /        \


# https://leetcode.com/problems/symmetric-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def f(p,q):
#     return (p is q) if not (p and q) else (p.val==q.val) and (f(p.left,q.right) and f(p.right,q.left))
           
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return f(root,root)


# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # if root:
        # #     if not(root.left or root.right):
        # #         return 1
        # #     if root.left:
        # #         ansleft = self.maxDepth(root.left)+1
        # #     if root.right: 
        # #         ansRight = self.maxDepth(root.right)+1
        # #     if root.left and root.right:
        # #         return max(ansleft,ansRight)
        # #     elif root.left and not root.right:
        # #         return ansleft
        # #     else:
        # #         return ansRight
        # return 1+max(self.maxDepth(root.right),self.maxDepth(root.left)) if root else 0