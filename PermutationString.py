'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Solution 1
from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = False
        permList = permutations(s1) 
        #logic ok but memory exceeds for large permutations
        permList = list(permList)
        strList = []
        for perm in list(permList):
            strList.append(''.join(perm))
        
        for item in strList:
            if item in s2:
                return True
                break

        return c
'''
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s1's permutation to be in s2
        if len1 > len2:
            return False
        
        # Count characters in s1 and the first window of s2
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len1])
        
        # Check if the counts match for the first window
        if s1_count == s2_count:
            return True
        
        # Slide the window over s2
        for i in range(len1, len2):
            # Add the new character to the window
            s2_count[s2[i]] += 1
            
            # Remove the leftmost character of the previous window
            s2_count[s2[i - len1]] -= 1
            
            # Remove the count from the dictionary if it becomes zero
            if s2_count[s2[i - len1]] == 0:
                del s2_count[s2[i - len1]]
            
            # Check if the counts match
            if s1_count == s2_count:
                return True
        
        return False
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        
        # If s1 is longer than s2, it's impossible for s1's permutation to be in s2
        if len1 > len2:
            return False
        
        # Count characters in s1 and the first window of s2
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len1])
        
        # Check if the counts match for the first window
        if s1_count == s2_count:
            return True
        
        # Slide the window over s2
        for i in range(len1, len2):
            # Add the new character to the window
            s2_count[s2[i]] += 1
            
            # Remove the leftmost character of the previous window
            s2_count[s2[i - len1]] -= 1
            
            # Remove the count from the dictionary if it becomes zero
            if s2_count[s2[i - len1]] == 0:
                del s2_count[s2[i - len1]]
            
            # Check if the counts match
            if s1_count == s2_count:
                return True
        
        return False
