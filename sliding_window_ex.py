# Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.
from typing import List


def check_subarray(arr: List[int], k: int):
    left = ans = sums = 0
    for right in range(len(arr)):
        sums += arr[right]
        while sums > k:
            sums -= arr[left]
            left += 1
    ans = max(ans, right-left+1)
    return ans


soln = check_subarray([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
print(soln)
