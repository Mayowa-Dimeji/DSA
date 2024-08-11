def better_compression(S):
    char_count = {}
    i = 0

    while i < len(S):
        char = S[i]
        i += 1

        count = 0
        while i < len(S) and S[i].isdigit():
            count = count * 10 + int(S[i])
            i += 1

        if char in char_count:
            char_count[char] += count
        else:
            char_count[char] = count

    charsorted = sorted(char_count.keys())
    compressed = ''.join(f'{char}{char_count[char]}' for char in charsorted)
    return compressed


# Test the function
print(better_compression('a3c9b2c1'))  # Output should be 'a3b2c10'
