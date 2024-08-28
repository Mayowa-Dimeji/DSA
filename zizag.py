def zigzag(s: str, numRows: int):
    ans = [[] for _ in range(numRows)]
    row = 0
    down = True

    for c in s:
        ans[row].append(c)

        if row == 0:
            down = True
        if row == numRows-1:
            down = False

        if down:
            row += 1
        else:
            row -= 1

    return ''.join(''.join(row) for row in ans)


s, numRows = "PAYPALISHIRING", 5
print(zigzag(s, numRows))
