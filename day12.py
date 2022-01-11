# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
# https://leetcode.com/problems/flood-fill/
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# https://www.spoj.com/problems/AGGRCOW/

# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# https://leetcode.com/problems/running-sum-of-1d-array/
# https://leetcode.com/problems/battleships-in-a-board/

#============================================================================================

# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

# from collections import Counter

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b,a%b)
    
# def hasGroupsSizeX(deck):
#         c= Counter(deck)
#         ans = c[deck[0]]
#         for num in set(deck):
#             if c[num] != ans:
#                 big,small = max(c[num],ans) , min(c[num],ans)
#                 g=gcd(big,small)
#                 if g==1:
#                     return False
#                 ans = g
#         return ans>1
# deck = [1,1,2,2,3,3,3,3]
# hasGroupsSizeX(deck)    


#============================================================================================

# https://leetcode.com/problems/flood-fill/

# def floodFill(img, sr, sc, newColor):
#         col = img[sr][sc]
        
#         if col == newColor:
#             return img
        
#         img[sr][sc] = newColor
        
#         if sr>0 and col == img[sr-1][sc]:
#             floodFill(img,sr-1,sc,newColor)
            
#         if sr<len(img)-1 and col == img[sr+1][sc]:
#             floodFill(img,sr+1,sc,newColor)
        
#         if sc>0 and col == img[sr][sc-1]:
#             floodFill(img,sr,sc-1,newColor)
        
#         if sc<len(img[0])-1 and col == img[sr][sc+1]:
#             floodFill(img,sr,sc+1,newColor)
        
#         return img         
# floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) 
















#============================================================================================
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# class Solution:
#     def findMin(self, nums):
#         if len(nums) == 1: return nums[0]
#         if nums[0] < nums[-1]: return nums[0]
#         low = 0
#         high = len(nums) - 1
#         while low <= high:
#             mid = (low + high) // 2
            
#             if nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]
            
#             if nums[mid - 1] > nums[mid]:
#                 return nums[mid]
            
#             if nums[low] < nums[mid]:
#                 low = mid + 1
            
#             else:
#                 high = mid - 1   























#============================================================================================
# https://www.spoj.com/problems/AGGRCOW/




# def func(mid , nums, C):
#     cow = 1
#     curr_pos = nums[0]
#     for i in range(1,len(nums)):
#         if(nums[i]-curr_pos > mid):
#             pos = nums[i]   
#             cow +=1
#             if(cow == C):
#                 return 1
#     return 0              




# def binary_search(nums,C):
#     low = 0
#     high = len(nums) -1
#     max = -1

#     while(low<=high):
#         mid = (low + high) // 2
#         if(func(mid,nums,C)==1):
#             if(mid>max):
#                 max=mid
#             low = mid+1
#         else:
#             high = mid
#     return max        


# if __name__ == "__main__":
#     N ,C = input().split()
#     position_Of_shelters = list(map(int,input().split()))
#     position_Of_shelters_sorted = sorted(position_Of_shelters)
#     res =  binary_search(position_Of_shelters_sorted,C)
#     print(res)









#============================================================================================
# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
















#============================================================================================
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

        # i = 0
        # j = len(nums)-1
        # while i<j:
        #     if nums[i] + nums[j] == target:
        #         return[i+1,j+1]
        #     elif nums[i] + nums[j] > target:
        #         j-=1
        #     else:
        #         i+=1
#------------------------------------------
        # m={}
        # for i,x in enumerate(nums):
        #     if target-x in m:
        #         print(m)
        #         return [m[target-x]+1,i+1]
        #     m[x] = i
#-----------------------------------------------------         
        
        # l=0
        # h=len(nums)-1
        # while l<h:
        #     mid = l+(h-l)//2
        #     if nums[l]+nums[h] == target:
        #         return [l+1,h+1]
        #     if nums[l] + nums[mid] > target:
        #         h=mid
        #     if nums[l]+nums[h] > target:
        #         h-=1
        #     if nums[l]+nums[h] < target:
        #         l+=1

















#============================================================================================
# https://leetcode.com/problems/running-sum-of-1d-array/




# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
        
#         for i in range(1,len(nums)):
#             nums[i] += nums[i-1]
#         return nums      




#============================================================================================
# https://leetcode.com/problems/battleships-in-a-board/



# def countBattleships(self, board: List[List[str]]) -> int:
#         count = 0
#         for r in range(len(board)):
#             for c in range(len(board[0])):
#                 if board[r][c] == 'X' and (r==0 or board[r-1][c]=='.') and (c==0 or board[r][c-1] == '.'):
#                     count+=1
#         return count


#============================================================================================
















































































