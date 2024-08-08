from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # If they don't overlap, add the current interval to the merged list
            merged.append(current)

    return merged


# Example usage
intervals = [[900, 1000], [930, 1100], [1500, 1600], [1530, 1700]]
print(merge_intervals(intervals))  # Output: [[900, 1100], [1500, 1700]]
