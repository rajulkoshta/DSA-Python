#     https://leetcode.com/problems/maximum-subarray/
#     https://leetcode.com/problems/powx-n/
#     https://leetcode.com/problems/rotate-image/
#     https://leetcode.com/problems/missing-number/
    
#     Take-Home Assignment (THA):
#     https://leetcode.com/problems/product-of-array-except-self/
#     https://leetcode.com/problems/3sum/
#     https://leetcode.com/problems/fibonacci-number/

#####################################################################
# https://leetcode.com/problems/maximum-subarray/


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_num =  max(nums)
#         if max_num < 0:
#             return max_num
#         curr_sum = 0
#         max_sum = 0
#         for num in nums:
#             curr_sum += num
#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#             if curr_sum < 0:
#                 curr_sum = 0
#         return max_sum       

########################################################################################
#  https://leetcode.com/problems/rotate-image/
# Approach: Reverse on Diagonal(transpose) and then Reverse Left to Right
# Intuition

# The most elegant solution for rotating the matrix is to firstly reverse the matrix around the main diagonal, and then reverse it from left to right. These operations are called transpose and reflect in linear algebra.
# Here is a visualization to help you see why this works.

# Bonus Question: What would happen if you reflect and then transpose? Would you still get the correct answer?

# Even though this approach does twice as many reads and writes as approach 1, most people would consider it a better approach because the code is simpler, and it is built with standard matrix operations that can be found in any matrix library.

# Complexity Analysis
# Let MM be the number of cells in the grid.
# Time complexity : O(M). We perform two steps; transposing the matrix, and then reversing each row. Transposing the matrix has a cost of O(M) because we're moving the value of each cell once. Reversing each row also has a cost of O(M), because again we're moving the value of each cell once.
# Space complexity :O(1) because we do not use any other additional data structures.
# ------------------------------------------------------------------------------------------
# Implementation
# USING FUNCTION CALLING

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         self.transpose(matrix)
#         self.reflect(matrix)
    
#     def transpose(self, matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

#     def reflect(self, matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(n // 2):
#                 matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
# ----------------------------------------------------------------------------------------
# class Solution:
#     def rotate(self, m: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         n = len(m)
#         for j in range(n):
#             for i in range(n//2):
#                 m[i][j],m[n-1-i][j] = m[n-1-i][j] , m[i][j]
#         for i in range(n):
#             for j in range(i+1,n):
#                 m[i][j],m[j][i]=m[j][i],m[i][j]
#         return m     

#----------------------------------------------------------------------------------------
# Approach: Rotate Groups of Four Cells
# Intuition
# Observe how the cells move in groups when we rotate the image.
# The corners all move We can iterate over each group of four cells and rotate them.

# Implementation

# class Solution:
    # def rotate(self, matrix: List[List[int]]) -> None:
    #     n = len(matrix[0])
    #     for i in range(n // 2 + n % 2):
    #         for j in range(n // 2):
    #             tmp = matrix[n - 1 - j][i]
    #             matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
    #             matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
    #             matrix[j][n - 1 - i] = matrix[i][j]
    #             matrix[i][j] = tmp


# Complexity Analysis

# Let M be the number of cells in the matrix.

# Time complexity : O(M), as each cell is getting read once and written once.

# Space complexity :O(1) because we do not use any other additional data structures.

############################################################################################

# https://leetcode.com/problems/powx-n/

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         isxneg,isnneg = x<0 , n<0
#         x ,n = abs(x) , abs(n)
#         if n==0:
#             return 1
#         if n==1:
#             return 1/x if isnneg else x
#         pwr = self.myPow(x,n//2)
#         ans = pwr*pwr if n%2==0 else pwr*pwr*x
#         if isxneg and n%2==1:
#             ans =-ans
#         if isnneg:
#             ans = 1/ans
#         return ans   

############################################################################################

#     https://leetcode.com/problems/missing-number/

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         return(n*(n+1)//2 - sum(nums))

#----------------------------------------------------------------------------------------

# using XOR / exclusive OR  operator:
 
#  0 0 - 0            properties : 
#  0 1 - 1            A XOR A = 0    
#  1 0 - 1            A XOR A XOR A = 0
#  1 1 - 0            A XOR 0 = 0 XOR A = A

#   n =len(nums)
#         x = nums[0]
#         for i in range(1,n):
#             x ^= nums[i]
#         for i in range(n+1):
#             x ^= i
#         return x    

############################################################################################

# Take-Home Assignment (THA):
#     https://leetcode.com/problems/product-of-array-except-self/
    
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         res = [1] * n
#         prefix = 1
#         for i in range(n):
#             res[i] = prefix
#             prefix *= nums[i]
#         post = 1
#         for i in range(n-1,-1,-1):
#             res[i] *= post
#             post *= nums[i]
#         return res








############################################################################################

#     https://leetcode.com/problems/3sum/

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

# Brute force approach
        # n = len(nums)
        # sol = []
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
        #                 sol.append([nums[i], nums[j], nums[k]]) 
        # return sol
            
#----------------------------------------------------------------------------
        
# another approach
        # counter  = Counter(nums)
        
        # nums=list(counter.keys())
        # triplets = set()
        
        # if counter[0]>=3 :
        #     triplets.add((0,0,0))
        # plus = [n for n in nums if n>0]    
        # minus = [n for n in nums if n<0]
        
        # print(plus,minus)
        
        # for a in plus:
        #     for b in minus:
        #         c = -(a+b)
                
        #         if c in counter and ((c!=a and c!=b) or counter[c] > 1):
        #             triplets.add(tuple(sorted([a,b,c])))
        # return triplets   


############################################################################################

#     https://leetcode.com/problems/fibonacci-number/


# class Solution:
#     def fib(self, n: int) -> int:
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         ans = self.fib(n-1) + self.fib(n-2)    
#         return ans

#----------------------------------------------------------------------------
#    without recursion:
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
        
#         a, b, c = 0, 1, 1
#         for _ in range(1,n):
#             c = a + b                
#             a, b = b, c
#         return c

# using list: 

# class Solution:
#     def fib(self, n: int) -> int:
#         f = [0,1]
#         for i in range(2,n+1):
#             f.append(f[i-1] + f[i-2])
#         return f[n]




############################################################################################
