
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://leetcode.com/problems/binary-tree-right-side-view/
# https://leetcode.com/problems/binary-tree-right-side-view/

#-------------------------------------------------------------------------------------------------------



# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root:
#             if root.val == p.val or root.val == q.val:
#                 return root
#             left, right = self.lowestCommonAncestor(root.left,p,q),self.lowestCommonAncestor(root.right,p,q)
#             if left and right:
#                 return root
#             return left if left else right
#         return None


#============================================================================================

# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def f(root):
#     if root:
#         left_depth, left_path = f(root.left)
#         right_depth, right_path = f(root.right)
#         return 1 + max(left_depth , right_depth) , max(left_path , right_path , left_depth + right_depth + 1)
#     return 0,0

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         return f(root)[1] - 1
        
#============================================================================================

# https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def f(root,m,y):
#     if root:
#         m[y] = root.val
#         f(root.left,m,y+1)
#         f(root.right,m,y+1)
    

# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         m = dict()
#         f(root,m,0)
#         return m.values()

#============================================================================================
# /binary-tree-left-side-view/




#============================================================================================

# /binary-tree-top-side-view/   abhi bana nahi hai dekhna padega ++++

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def f(root,m,x,y):
    if root:
        m[x] = [root.val,y]
        f(root.left,m,x-1,y+1)
        f(root.right,m,x+1,y+1)

class Solution:
    def topSideView(root) :
        m=dict()
        f(root,m,0,0)
        val = []
        values = list(m.values())
        for i in range(len(values)):
           val = values[i][0]
        return val   

root = Node(1,
            Node(2,Node(None),Node(5)),
            Node(3,Node(None),Node(4)))
print(Solution.topSideView(root))