class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:  # Added type hints
        # Handle edge cases where nums2 is empty (nums1 is already sorted)
        if n == 0:
            return
        
        # Pointers for nums1, nums2, and the merge position
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy remaining elements of nums2 to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]
