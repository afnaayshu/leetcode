'''
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 
Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
'''

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []  
        # Create a sorted version of the array
        arr2 = sorted(arr)
        # Create a dictionary to store the rank of each number
        rank_dict = {}
        rank = 1
        
        for num in arr2:
            if num not in rank_dict:
                rank_dict[num] = rank
                rank += 1
        
        # Map each number in the original array to its rank
        return [rank_dict[num] for num in arr]
