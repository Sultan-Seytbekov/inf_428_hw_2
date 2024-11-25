class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:  # Added type hints
        set1 = set(nums1)  # Convert nums1 to a set
        set2 = set(nums2)  # Convert nums2 to a set
        result = set1.intersection(set2)  # Find the intersection
        return list(result)  # Convert the result back to a list
