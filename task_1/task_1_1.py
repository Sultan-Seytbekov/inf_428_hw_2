class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:  # Added type hints
        if len(nums) == 0:  # Explicitly check if the list is empty
            return 0

        max_length = 1  # Tracks the longest LCIS
        current_length = 1  # Tracks the current LCIS length

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Current number is larger than the previous
                current_length += 1
            else:
                max_length = max(max_length, current_length)
                current_length = 1  # Reset the current sequence

        # Final comparison to ensure the last sequence is considered
        return max(max_length, current_length)
