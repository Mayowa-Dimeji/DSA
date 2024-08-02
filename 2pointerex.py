# Example 1: Given a string s, return true if it is a palindrome, false otherwise.

# A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".
def check_if_palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
def check_sum(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        curr = arr[left] + arr[right]
        if curr == target:
            return True
        elif curr < target:
            left += 1
        else:
            right -= 1

    return False

# Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.


def sorted_arr(arr1, arr2):
    i = j = 0
    arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1
    return arr

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, while maintaining the relative order of the remaining characters. For example, "ace" is a subsequence of "abcde" while "aec" is not.


def is_subsequence(s, t):
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
