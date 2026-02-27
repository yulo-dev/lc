class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1) 
        n = len(nums2) 
        half_length = (m + n + 1) // 2 # 這個+1的設計是 當總長是 odd 時，左半邊比右半邊多 1 個元素

        left = 0
        right = m

        while left <= right:
            i = left + (right - left) // 2   # i = 從 nums1 拿幾個放左邊, num1的切點
            j = half_length - i              # j = 從 nums2 拿幾個放左邊, num2的切點, 由「左半邊應該有多少元素」減去 nums1 左邊已經拿了多少元素 i 得到


            #這四個點是每個 array 的「切口左右兩邊最靠近切口的值」
            #例如
                #i = 2
                #j = 2
                #nums1: [1, 3 | 8]
                #nums2: [7, 9 | 10, 11]
            #則
                #l1 = 3
                #r1 = 8
                #l2 = 9
                #r2 = 10
            l1 = nums1[i - 1] if i > 0 else float("-inf") #l1 = nums1 左半邊最後一個
            r1 = nums1[i] if i < m else float("inf")      #r1 = nums1 右半邊第一個
            l2 = nums2[j - 1] if j > 0 else float("-inf") #l2 = nums2 左半邊最後一個
            r2 = nums2[j] if j < n else float("inf")      #r2 = nums2 右半邊第一個

            #因為兩個陣列本來就各自 sorted 所以如果你已經知道l1 <= r2 and l2 <= r1, 就代表：左邊全部都 <= 右邊全部
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