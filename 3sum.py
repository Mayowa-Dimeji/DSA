'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
    
    
    [0,0,-1,2,2,1,1]
    [[0,-1,1],[0,-1,1]]
    
     [-1,0,1,2,-1,-4]
     
     [-1,3,1,2,0,-4]
     
     
     
     sort nums
     compare elem at i with 2 values at left, end
     loop again for initiation of left,right
     
         if it is put triplet in our ans
         if it less move left
         if it more move our right
     
     
     
'''
# -(x+y)=z
# enumerate nums

# iterte through nums, get elem at index i and index i+1
# check if z is in map and index is not same x or y, put it in ans array sorted
# return  a set of the ans


def fn(nums):
    nums = list(sorted(nums))
    print(nums)
    ans = []
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        for _ in range(left, right):
            my_sum = nums[i]+nums[left]+nums[right]
            if my_sum == 0:
                ans.append([nums[i], nums[left], nums[right]])
            elif my_sum < 0:
                left += 1
            else:
                right -= 1
    # convert to tuple to make it hashable
    ans = set(tuple(triplet) for triplet in ans)
    # convert back to list
    ans = [list(triplet) for triplet in ans]
    return ans


print(fn([-1, 3, 1, 2, 0, -4]))
# print([-1,0,1,2,-1,-4].sort())
