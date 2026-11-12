class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Input:
        # Two sorted integer arrays
        # m, n: numbers of valid elements

        # Output:
        # Modify nums1 in place; return None

        # Clarifications:
        # - Only the first m elements of nums1 are valid?
        # - Is O(1) extra space expected?

        # Edge cases:
        # m = 0
        # n = 0
        # Duplicate values
        # Negative numbers and valid zeros

        # Approach:
        # I'll use two pointers, starting from the last valid elements of nums1 and nums2. 
        # I'll compare the two values and place the larger one at the end of nums1. 
        # Then I'll move the corresponding pointer backward and continue until the merge is complete.

      
        left = m-1
        right = n-1

        for i in range(len(nums1)-1, -1, -1):
            if left >= 0 and right >= 0 and nums1[left] > nums2[right]: 
                nums1[i] = nums1[left]
                left -= 1

            elif left >= 0 and right >= 0 and nums1[left] <= nums2[right]:
                nums1[i] = nums2[right]
                right -= 1
            
            elif left < 0 and right >= 0:
                nums1[i] = nums2[right]
                right -= 1

            elif left >= 0 and right == 0:
                nums1[i] = nums1[left]
                left -= 1
