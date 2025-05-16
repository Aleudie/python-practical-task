#!/usr/bin/env python3

from collections import Counter

"""
Task 1.4. Given an input string, count occurrences of all characters within a string 
(e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
"""

class Solution:
    def count_letters(self, string: str) -> dict[str, int]:
        letter_count = Counter()
        string = string.lower()

        for char in string:
            if char.isalpha():
                letter_count[char] += 1
        return letter_count
    
string = "pythonnohtyppy"
solution = Solution()
print(solution.count_letters(string))