class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #確保 nums1 是短的，這樣二分搜尋更快，且 j 不會變負數
        #如果 nums1 很長，而 nums1 的切點 i 選得很大，那麼為了湊齊總數，nums2 的切點 j 可能會變成 負數。
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1) 
        n = len(nums2)

        left = 0
        right = m
        half_len = (m + n + 1) // 2 #左半部需要的總人數

        while left <= right:
            i = (left + right) // 2     #在 nums1 切一刀 (左邊有 i 個人) #算是nums1的mid
            j = half_len - i            # 在 nums2 切一刀 (左邊有 j 個人)

            # --- 抓出四個關鍵數值 (處理邊界細節) ---
            # 如果 i == 0，代表 nums1 左邊沒人，用 -inf 代替
            l1 = nums1[i-1] if i > 0 else float('-inf')
            # 如果 i == m，代表 nums1 右邊沒人，用 +inf 代替
            r1 = nums1[i] if i < m else float('inf')
            
            l2 = nums2[j-1] if j > 0 else float('-inf')
            r2 = nums2[j] if j < n else float('inf')
            
            # --- 判斷切點是否正確 (根據「值」來判斷) ---
            if l1 <= r2 and l2 <= r1:
                # 找到了完美的切分線！
                if (m + n) % 2 == 1:
                    # 如果總數是奇數，中位數就是左邊最大的那個
                    return max(l1, l2)
                else:
                    # 如果總數是偶數，中位數是 (左邊最大 + 右邊最小) / 2
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            
            elif l1 > r2:
                # nums1 出的數太大了，切點 i 要往左移
                right = i - 1
            else:
                # nums1 出的數太小了，切點 i 要往右移
                left = i + 1

        return 0.0