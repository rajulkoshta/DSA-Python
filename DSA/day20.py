 





# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder, inorder):
        # if not preorder or not inorder:
        #     return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # SOLUTION USING MAP

        # inorder_dict = {}
        # for i, num in enumerate(inorder):
        #     inorder_dict[num] = i
        # preorder_iter = iter(preorder)

        # def helper(start, end):
        #     if start > end:
        #         return None
        #     root_val = next(preorder_iter)
        #     root = TreeNode(root_val)
        #     index = inorder_dict[root_val]
        #     root.left = helper(start, index-1)
        #     root.right = helper(index+1, end)
        #     return root
        
        # return helper(0, len(inorder) - 1)

#============================================================================================


# https://leetcode.com/problems/leaf-similar-trees/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def leaf_node(root):
#         if root:
#             if not root.left and not root.right:
#                 return [root.val]
#             return leaf_node(root.left) + leaf_node(root.right)
#         return [] 
        
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:  
#         list1 = leaf_node(root1)
#         list2 = leaf_node(root2)
#         return list1 == list2


#============================================================================================
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
#         q = deque([None,root])
#         avg = []
#         curr = []
#         while True:
#             node = q.pop()
#             if not node:
#                 avg.append(sum(curr)/len(curr))
#                 if len(q)<1:
#                     return avg
#                     return
#                 curr=[]
#                 q.appendleft(None)
#                 continue
#             curr.append(node.val)            
#             if node.left:
#                 q.appendleft(node.left)
#             if node.right:
#                 q.appendleft(node.right)



#============================================================================================
#     ------------  |      |        /\
#          |        |      |       /  \
#          |        |------|      /----\
#          |        |      |     /      \
#          |        |      |    /        \



# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not postorder or not inorder:
#             return None

#         val = postorder.pop()
#         root = TreeNode(val)
#         mid = inorder.index(val)
#         root.right = self.buildTree(inorder[mid+1:],postorder)
#         root.left = self.buildTree(inorder[:mid],postorder)
#         return root    
        
        # inorder_dict = {}
        # for i, num in enumerate(inorder):
        #     inorder_dict[num] = i

        # def helper(start, end):
        #     if start > end:
        #         return None
        #     root_val = postorder.pop()
        #     root = TreeNode(root_val)
        #     index = inorder_dict[root_val]
        #     root.right = helper(index+1, end)
        #     root.left = helper(start, index-1)
        #     return root
        
        # return helper(0, len(inorder) - 1)


#============================================================================================


# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Approach - 1
# Using single ended queue and reverse. Although we are using deque we are utilizing only single ended queue functionality here.

# def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
# 	if not root: return []
# 	queue = collections.deque([root])
# 	res = []
# 	even_level = False
# 	while queue:
# 		n = len(queue)
# 		level = []
# 		for _ in range(n):
# 			node = queue.popleft()
# 			level.append(node.val)
# 			if node.left:
# 				queue.append(node.left)
# 			if node.right:
# 				queue.append(node.right)
# 		if even_level:
# 			res.append(level[::-1])
# 		else:
# 			res.append(level)
# 		even_level = not even_level
# 	return res

#============================================================================================

# Appraoch - 2
# Using single ended queue and initializing array instead of reversing.

# def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
# 	if not root: return []
# 	queue = collections.deque([root])
# 	res = []
# 	even_level = False
# 	while queue:
# 		n = len(queue)
# 		level = [0] * n # initalize the array since we know the length
# 		for i in range(n):
# 			node = queue.popleft()
# 			if node.left:
# 				queue.append(node.left)
# 			if node.right:
# 				queue.append(node.right)
# 			if even_level:
# 				level[n-1-i] = node.val
# 			else:
# 				level[i] = node.val
# 		res.append(level)
# 		even_level = not even_level

# 	return res

#============================================================================================

# Approach - 3
# Using the double ended queue functionality. We pop from left in odd levels and pop from right in even levels. Trick is to flip the order of left and right when we are appending from left.

# def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
# 	if not root: return []
# 	queue = collections.deque([root])
# 	res = []
# 	even_level = False
# 	while queue:
# 		n = len(queue)
# 		level = []
# 		for i in range(n):
# 			if even_level:
# 				# pop from right and append from left.
# 				node = queue.pop()
# 				# to maintain the order of nodes in the format of [left, right, left, right] 
# 				# we push right first since we are appending from left
# 				if node.right: queue.appendleft(node.right)
# 				if node.left: queue.appendleft(node.left)
# 			else:
# 				# pop from left and append from right
# 				node = queue.popleft()
# 				# here the order is maintained in the format [left, right, left, right] 
# 				if node.left: queue.append(node.left)
# 				if node.right: queue.append(node.right)
# 			level.append(node.val)
# 		res.append(level)
# 		even_level = not even_level
# 	return res

#============================================================================================

# Approach - 4
# Using deque for each level instead of list.

# def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
#     if not root: return []
#     res = []
#     queue = collections.deque([root])
#     even_level = False
#     while queue:
#         n = len(queue)
#         level = collections.deque()
#         for _ in range(n):
#             node = queue.popleft()
#             if even_level:
#                 level.appendleft(node.val)
#             else:
#                 level.append(node.val)
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         res.append(list(level))
#         even_level = not even_level
#     return res


