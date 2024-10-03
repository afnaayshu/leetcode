'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters. Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Dictionary to count occurrences of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        length = 0
        odd_found = False

        # Iterate over the character counts
        for count in char_count.values():
            # If the count is even, add all occurrences to the palindrome length
            if count % 2 == 0:
                length += count
            else:
                # If odd, add the largest even part (count - 1)
                length += count - 1
                odd_found = True

        # If there's any odd character count, we can place one in the center
        if odd_found:
            length += 1

        return length
