# You are given two points on a 2D plane: a starting point
# (
#     𝑥
#     1,
#     𝑦
#     1
# )
# (x
#  1
#  ​, y
#  1
#  ​
#  ) and a destination point
# (
#     𝑥
#     2,
#     𝑦
#     2
# )
# (x
#  2
#  ​, y
#  2
#  ​
#  ). A bot is located at the starting point and can move using the following two types of moves:

# Right Move: From
# (
#     𝑥,
#     𝑦
# )
# (x, y) to
# (
#     𝑥
#     +
#     𝑦,
#     𝑦
# )
# (x+y, y).
# Up Move: From
# (
#     𝑥,
#     𝑦
# )
# (x, y) to
# (
#     𝑥,
#     𝑥
#     +
#     𝑦
# )
# (x, x+y).
# You need to determine if it is possible for the bot to reach the destination point
# (
#     𝑥
#     2,
#     𝑦
#     2
# )
# (x
#  2
#  ​, y
#  2
#  ​
#  ) starting from the point
# (
#     𝑥
#     1,
#     𝑦
#     1
# )
# (x
#  1
#  ​, y
#  1
#  ​
#  ).
def canReach(x1: int, y1: int, x2: int, y2: int) -> str:
    # Base case: if the starting coordinates are the same as the destination coordinates
    if x1 == x2 and y1 == y2:
        return 'Yes'  # It's possible to reach the destination

    # Recursive cases:
    # Try moving right (adding y-coordinate to x-coordinate)
    if x1 < x2 and canReach(x1 + y1, y1, x2, y2) == 'Yes':
        return 'Yes'

    # Try moving up (adding x-coordinate to y-coordinate)
    if y1 < y2 and canReach(x1, y1 + x1, x2, y2) == 'Yes':
        return 'Yes'

    # If none of the above conditions are met, it's not possible to reach the destination
    return 'No'


def iteratecanReach(x1: int, y1: int, x2: int, y2: int) -> str:
    while x2 >= x1 and y2 >= y1:
        if x2 == x1 and y2 == y1:
            return "Yes"

        # If x2 is greater than y2, the last move was likely adding y to x, so subtract y2 from x2
        if x2 > y2:
            x2 -= y2
        # Otherwise, the last move was likely adding x to y, so subtract x2 from y2
        else:
            y2 -= x2

    return "No"
