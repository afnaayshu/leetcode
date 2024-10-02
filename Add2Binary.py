'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str( bin(int(a,2)+int(b,2)))[2:]

  #TC : O(n)
