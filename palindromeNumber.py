'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''
#solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numbers and numbers ending with 0 are not palindrome
        if x<0 or(x%10==0 and x!=0):
            return False
        
        rev_half = 0
        while(x>rev_half):
            rev_half = rev_half*10 + x%10
            x//=10

        return rev_half == x or rev_half//10 == x

  #Time complexity O(n)
