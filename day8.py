#     https://leetcode.com/problems/two-sum/
#     https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#     https://leetcode.com/problems/remove-duplicates-from-sorted-array/

#     Take-Home Assignment (THA):

#     https://leetcode.com/problems/contains-duplicate/
#     https://leetcode.com/problems/valid-anagram/
#     https://leetcode.com/problems/next-permutation/


# *******************************************************************************

# two sum

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         m = {}
#         for i,x in enumerate(nums):
#             if target-x in m:
#                 print(m)
#                 return [m[target-x],i]
#             m[x] = i

#----------------------------------------------------------------------  

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return[i,j]
        

# *******************************************************************************

# best-time-to-buy-and-sell-stock

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_till_now = 10001
#         best_profit = 0
#         for i in prices:
#             if best_profit < i - min_till_now:
#                 best_profit = i - min_till_now
#             elif min_till_now > i:
#                 min_till_now = i
#         return best_profit
        
#----------------------------------------------------------------------  
                
#         min_till_now = prices[0]
#         best_profit = 0
#         for i in range(len(prices)):
#             if best_profit < prices[i] - min_till_now:
#                 best_profit = prices[i] - min_till_now
#             elif min_till_now > prices[i]:
#                 min_till_now = prices[i]
#         return best_profit    

# *******************************************************************************

# remove-duplicates-from-sorted-array

# (two pointer approch)

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums)==0:
#             return 0
#         left=0
#         right=1
#         while right < len(nums):
#             if nums[right] - nums[left]:
#                 if right - left == 1:
#                     left +=1
#                 elif right -left > 1 :
#                     nums[left+1]= nums[right]
#                     left +=1
#             right+=1
#         return left+1

# ------------------------------------------------------------------

        # c=0
        # for i in range(len(nums)):
        #     if  nums[c] != nums[i]:
        #         c+=1
        #         nums[c]=nums[i]
        # return c+1     

# *******************************************************************************

#     https://leetcode.com/problems/contains-duplicate/

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
        
        # if len(nums) > len(set(nums)):
        #     return True
        # else:
        #     return False
    
# ------------------------------------------------------------------
         # [1,2,3,1]
         # {1:2 , 2:1 , 3:1}
        # dict={}
        # for index, number in enumerate(nums):
        #     if number not in dict:
        #         dict[number] = index
        #     else:
        #          return True

# ------------------------------------------------------------------
        
        # hash={}
        # for i in nums:
        #     if i in hash:
        #         return True
        #     else:
        #         hash[i]=1
        
# ------------------------------------------------------------------
        
        # nums = sorted(nums)
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False 
                       
# *******************************************************************************

#     https://leetcode.com/problems/valid-anagram/

#     def isAnagram(s, t):
# ------------------------------------------------------------------

# char method        
#         if len(s) != len(t):
#             return False
#         for char in set(s):
#             if s.count(char)!= t.count(char):
#                 return False
#         return True

# ------------------------------------------------------------------

# sorting (nlogn)
            # return sorted(s) == sorted(t)
# ------------------------------------------------------------------
    
# hashmap (n)    
#             map_s = {}
#             map_t = {}
#             for i in s:
#                 map_s[i] = map_s.get(i,0) + 1
            
#             for i in t:
#                 map_t[i] = map_t.get(i,0) + 1
#             return map_s == map_t    

# *******************************************************************************

#     https://leetcode.com/problems/next-permutation/

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

# first method buggy code - need to work on it
#         i=len(nums)-1
        
# find first decresing element
          
#         while i>0:
#             if nums[i]>nums[i-1]:
#                 break
#             i-=1    
            
#         i-=1  
#         if i==-1:
#             nums[:] = sorted(nums)
#             return
#         else:
# closest next greater element towards right 
#             j = len(nums)-1
#             while j>0 and nums[j] < nums[i]:
#                 j-=1
#             # swap
#             nums[i] , nums[j] = nums[j] ,nums[i]
        
# reverse the rest element
#             # nums[i+1:] = nums[i+1:][::-1]
#             nums[i+1:] = sorted(nums[i+1:])
#             return
            
# ------------------------------------------------------------------
        # resolved code
            
        # i=len(nums)-2
        # while i>-1:
        #     if nums[i]<nums[i+1]:
        #         j=len(nums)-1
        #         while j>i:
        #             if nums[j] > nums[i]:
        #                 break
        #             j-=1
        #         nums[i],nums[j] = nums[j],nums[i]
        #         break
        #     i-=1
        # nums[i+1:] = reversed(nums[i+1:])

# *******************************************************************************

