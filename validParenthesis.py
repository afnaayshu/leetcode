'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type

'''

class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')': '(', ']': '[', '}': '{'}
        stack = []  # Stack to hold opening brackets

        for char in s:
            if char in bracketMap:  # If it's a closing bracket
                # Pop the top of the stack if not empty, otherwise set top as a dummy value
                top = stack.pop() if stack else '0'
                # If the top doesn't match the corresponding opening bracket, return False
                if bracketMap[char] != top:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets are matched; otherwise, return False
        return not stack
