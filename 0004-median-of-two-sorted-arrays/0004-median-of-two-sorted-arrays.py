class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #I swap the arrays to ensure that nums1 is always the shorter one. 
        #This is crucial because our binary search is performed on the range of the first array.
        #By ensuring nums1 is shorter, we guarantee that the index j (calculated as half_length - i) will always be 
        #a valid index in nums2. If nums1 were longer, j could potentially be negative, leading to index out-of-bounds errors.
        #This also optimizes the time complexity to O(log(min(m, n))) instead of O(log(m+n)). 
        #Since we binary search over the shorter array, it results in fewer iterations.

        #或是

        #First, I'll perform a quick check to make sure nums1 is the shorter array. This is a standard optimization for this 
        #algorithm to ensure the derived index j remains within a positive range and to achieve the most efficient log-time 
        #complexity based on the smaller input.
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

            l1 = nums1[i-1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < m else float("inf")
            l2 = nums2[j-1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < n else float("inf")

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 1:
                    #這邊是抓max(l1, l2) 而不是min(r1, r2) 關鍵在於我們對 half_length 的定義
                    #half_length = (m + n + 1) // 2 
                    #當總數 (m + n) 是奇數時，這個 +1 的操作會讓左半部比右半部多出一個數字
                    #所以既然左邊比較多，那個「正中間」的中位數就一定會落在左邊這區
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                right = i - 1
            else:
                left = i + 1

        return 0.0