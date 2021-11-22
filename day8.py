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







# *******************************************************************************

#     https://leetcode.com/problems/next-permutation/








# *******************************************************************************

