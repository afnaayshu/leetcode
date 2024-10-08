'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
'''
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Extract all letters from the string
        letters = [char for char in s if char.isalpha()]
        
        # Create a list to build the result
        result = []
        
        # Traverse the original string
        for char in s:
            if char.isalpha():
                # If it's a letter, pop the last letter from the reverse list
                result.append(letters.pop())
            else:
                # If it's not a letter, keep it in the same position
                result.append(char)
        
        # Join the list into a string and return the result
        return ''.join(result)
