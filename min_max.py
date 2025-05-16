#!/usr/bin/env python3

"""
Task 1.2 Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.
"""

class Solution:
    def min_max(self, lst: list[int]) -> tuple:
        if not lst:
            raise ValueError("The list is empty")
        return min(lst), max(lst)
    
    def to_tuple(self, lst: list[int]) -> tuple:
        if not lst:
            raise ValueError("The list is empty")
        return tuple(set(lst))

lst = [1, 7, 1, 3, 2, 2, 5, 4, 6, 8, 9, 0, 10, 0, 0, 0, 0, -2, -23, 55, 11, 12, 13, 14, 15]
solution = Solution()

min_value, max_value = solution.min_max(lst)
tupl = solution.to_tuple(lst)

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")
print(f"Tuple: {tupl}")