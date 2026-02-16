class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1) 
        n = len(nums2) 
        half_length = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = left + (right - left) // 2
            j = half_length - i

            l1 = nums1[i - 1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < m else float("inf")
            l2 = nums2[j - 1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < n else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    return max(l1, l2) 
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                right = i - 1
            else:
                left = i + 1

        return 0.0



#The goal is to find the median of two sorted arrays in logarithmic time, specifically O(log(min(m, n))). Instead of merging #the arrays, I'm using a binary search approach to ＊＊＊find the correct partition point＊＊＊ in the smaller array.


#First, I ensure that nums1 is the shorter array. This guarantees that our binary search runs on the smaller search space and #prevents index out-of-bounds for the second array.

#I use a binary search to find a partition i in nums1. The partition j in nums2 is then calculated such that the total number #of elements on the left side is exactly half of the combined length.

#I define four variables: l1, r1 from the first array, and l2, r2 from the second. These represent the elements immediately #surrounding our cut.
#The partition is correct if l1 <= r2 and l2 <= r1. This ensures that every element on the left side is smaller than or equal #to every element on the right side across both arrays.
#To handle edge cases where a partition falls outside the array bounds, I use positive and negative infinity.
    #Once the correct partition is found:
        #If the total length is odd, the median is simply the maximum of the left elements (max(l1, l2)).
        #If it's even, it's the average of the maximum on the left and the minimum on the right."