'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1  # Adjust high to be the last valid index
        
        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid

            if nums[mid] == target:
                return mid  # If target is found, return its index

            elif nums[mid] < target:
                low = mid + 1  # Ignore the left half

            else:
                high = mid - 1  # Ignore the right half
        
        # If target is not found, return the position where it would be inserted
        return low
