'''
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
'''
class Solution:
    def findComplement(self, num: int) -> int:
        numbin = bin(num)
        numbin = numbin[2:]
        complement = ""
        for i in range(len(numbin)):
            if numbin[i] == '1' :
                complement += '0'
            else :
                complement += '1'
        
        
        return int(complement,2)

