#     https://leetcode.com/problems/set-matrix-zeroes/
#     https://leetcode.com/problems/merge-intervals/
#     https://leetcode.com/problems/container-with-most-water/
    
#     THA:
#     https://leetcode.com/problems/final-value-of-variable-after-performing-operations
#     https://leetcode.com/problems/non-overlapping-intervals/
#     https://leetcode.com/problems/insert-interval/
#     https://leetcode.com/problems/build-array-from-permutation/

#============================================================================================

#     https://leetcode.com/problems/set-matrix-zeroes/

# class Solution:
#     def setZeroes(self, a: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """

        # NEED MORE WORK ON THIS APROUCH
        # m,n = len(matrix),len(matrix[0])
        # row = col = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             row.add(i)
        #             col.add(j)
        # for k in row:
        #     for i in range(n):
        #         matrix[k][i]=0
        # for k in col:
        #     for i in range(m):
        #         matrix[i][k]=0
        # return matrix        
#---------------------------------------------
# # ANOTHER APPROACH 
# def setZeros(a):    
#         m,n=len(a),len(a[0])
        
#         r,c = False,False
#         for i in range(m):
#             if not a[i][0]:
#                 c=True
                
#         for j in range(n):
#             if not a[0][j]:
#                 r=True
                
#         for i in range(m):
#             for j in range(n):
#                 if not a[i][j]:
#                     a[i][0]=0
#                     a[0][j]=0
        
#         for i in range(1,m):
#             if not a[i][0]:
#                 for j in range(1,n):
#                     a[i][j]=0
                    
#         for j in range(1,n):
#             if not a[0][j]:
#                 for i in range(1,m):
#                     a[i][j]=0
                    
#         if c:
#             for i in range(m):
#                 a[i][0] = 0
#         if r:
#             a[0] =[0]*n
#         return a 
# print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

#============================================================================================

#     https://leetcode.com/problems/container-with-most-water/

#     def maxArea(height):
#         max_water = 0
#         l=0
#         r=len(height)-1
#         while l<=r:
#             hl,hr = height[l],height[r]
#             max_water = max(max_water, min(hl,hr)*(r-l))
#             if min(hl,hr)*(r-l) > max_water:  #  } - optional
#                 max_water = min(hl,hr)*(r-l)  #  } - ^
#             if hr >= hl:
#                 l+=1
#             if hr<=hl:
#                 r-=1
#         return max_water   
# nums=[1,8,6,2,5,4,8,3,7]
# print(maxArea(nums)) 



#============================================================================================

#     https://leetcode.com/problems/merge-intervals/


# def merge(intervals):
#         intervals = sorted(intervals,key= lambda x : x[0])
#         res=[]
#         curr = intervals[0]
#         for nextInterval in intervals:
#             if nextInterval[0] <= curr[1]:
#                 if nextInterval[1] > curr[1]:
#                     curr[1] = nextInterval[1]
#             else:
#                 res.append(curr)
#                 curr=nextInterval
#         res.append(curr) 
#         return res
# print(merge([[1,3],[2,6],[8,10],[15,18]]))        

#============================================================================================

# THA

# https://leetcode.com/problems/final-value-of-variable-after-performing-operations

# class Solution:
#     def finalValueAfterOperations(self, operations: List[str]) -> int:
#         x=0
#         for op in operations:
#             if op == "X++":
#                 x=x+1
#             elif op == "++X":
#                 x=x+1
#             elif op == "X--":
#                 x=x-1    
#             elif op == "--X":
#                 x=x-1    
#         return x

#============================================================================================

# https://leetcode.com/problems/non-overlapping-intervals/

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals = sorted(intervals,key= lambda x : x[0])
#         count=0
#         curr = intervals[0][1]
#         for i in range(1,len(intervals)):
#             if intervals[i][0] < curr:
#                 curr = min(curr,intervals[i][1])
#                 count+=1
#             else:
#                 curr = intervals[i][1]           
#         return count



















#============================================================================================

# https://leetcode.com/problems/insert-interval/


# class Solution:
#     def insert(self, intervals, newInterval):
#         intervals.append(newInterval)
#         intervals = sorted(intervals,key= lambda x : x[0])
#         res=[]
#         curr = intervals[0]
#         for nextInterval in intervals:
#             if nextInterval[0] <= curr[1]:
#                 if nextInterval[1] > curr[1]:
#                     curr[1] = nextInterval[1]
#             else:
#                 res.append(curr)
#                 curr=nextInterval
#         res.append(curr) 
#         return res

#============================================================================================

# https://leetcode.com/problems/build-array-from-permutation/

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans=[]
#         for i in range(0,len(nums)):
#             ans.append(nums[nums[i]])
#         return ans





























#============================================================================================
