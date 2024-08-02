# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
from typing import List


def reverse_string(s):
    left = 0
    right = len(s)-1

    while left < right:
        currleft = s[left]
        currright = s[right]

        s[left] = currright
        s[right] = currleft
        left += 1
        right -= 1


# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.


# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


    def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        ans = [0]*n
        pos = n-1

        while left <= right:
            left_square = nums[left]**2
            right_square = nums[right]**2
            if left_square > right_square:
                ans[pos] = left_square
                left += 1
            else:
                ans[pos] = right_square
                right -= 1
            pos -= 1

        return ans

    myvar = sortedSquares([-4, -1, 0, 3, 10])
    print(myvar)
