# Question:

# Consider a string S that is a series of characters, each followed by its frequency as an integer. The string is not compressed correctly, so there may be multiple occurrences of the same character. A properly compressed string will consist of one instance of each character in alphabetical order followed by the total count of that character within the string.

# Example:

# Given the string 'a3c9b2c1', there are two instances where 'c' is followed by a count: once with 9 occurrences, and again with 1. It should be compressed to 'a3b2c10'.
def better_compression(S):
    char_count = {}
    i = 0

    while i < len(S):
        char = S[i]
        count = int(S[i+1])

        if char in char_count:
            char_count[char] = char_count[char]+count
        else:
            char_count[char] = count
        i += 2
    charsorted = sorted(char_count.keys())
    compressed = ''.join(f'{char}{char_count[char]}' for char in charsorted)
    return compressed


print(better_compression('a3c9b2c1'))
