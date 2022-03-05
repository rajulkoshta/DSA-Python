# THA

# https://leetcode.com/problems/search-insert-position/


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums)-1
#         while low <=high:
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 low=mid+1
#             else :
#                 high=mid-1
#         return low   

# https://leetcode.com/problems/binary-search/


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums)-1
#         while low <= high :
#             mid=(low+high)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 low = mid+1
#             else :
#                 high = mid-1
#         return -1          
########################################################################################

# EXTRAS

# - [Square Root](https://leetcode.com/problems/sqrtx/)
# - [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
# - [First Bad Version](https://leetcode.com/problems/first-bad-version/)
# - [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
# - [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
# - [Arranging Coins(Easy)](https://leetcode.com/problems/arranging-coins/)
# - [Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
# - [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)
# - [Search Insert Position](https://leetcode.com/problems/search-insert-position/)
# - [Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)
# - [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)
# - [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
# - [Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
# - [Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/)
# - [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/)
# - [Special Array With X Elements Greater Than or Equal X](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/)
# - [Binary Search](https://leetcode.com/problems/binary-search/)

#------------------------------------------------------------------------------------

# https://leetcode.com/problems/sqrtx/

# class Solution:
# def mySqrt(self, x: int) -> int:
        # low=1
        # high = x
        
        # if x==0 or x==1:
        #     return x
        
        # while low<=high:
        #     mid=(low+high)// 2
        #     if mid**2 == x:
        #         return mid
        #     elif mid**2 < x:
        #         low=mid+1
        #         ans=mid
        #     else :
        #         high=mid-1
        # return ans  



# def mySqrt(x):
#         if(x==0 or x==1):
#             return x
#         i=result=1
#         while (result <= x):
#                 i+=1
#                 result=i*i
#         return i-1

# print(mySqrt(9))        

########################################################################################
# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# class Solution:
#     def guessNumber(self, n: int) -> int:
#         low=1
#         high=n
#         while low<=high:
#             mid =(low+high)//2
#             pick = guess(mid)
#             if pick == 0:
#                 return mid
#             elif pick > 0:
#                 low = mid+1
#             else:
#                 high=mid-1
#         return -1       


########################################################################################

# - [First Bad Version](https://leetcode.com/problems/first-bad-version/)

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

# class Solution:
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         low = 1
#         high = n
#         while low<high:
#             mid = int(low+(high-low)/2)
#             if isBadVersion(mid):
#                 high = mid
#             else:
#                 low = mid+1
#         return high       

########################################################################################
