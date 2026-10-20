# 1. Two Sum
# Brute Force Approach
# Time Complexity: O(n^2) because every pair is checked
# Space Complexity: O(1) because no extra space is used
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
             for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
# Hash Map Approach
# Time Complexity: O(n) because we traverse the list containing n elements only once. Each look up in the table costs only O(1) time.
# Space Complexity: O(n) because we store up to n elements in the hash table.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i