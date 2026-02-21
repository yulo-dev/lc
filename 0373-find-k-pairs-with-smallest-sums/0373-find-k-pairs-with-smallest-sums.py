class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        h = []
        
        # 只需要前 min(k, len(nums1)) 條「列」的起點 (i,0)
        # 1. 初始化：每一列的「排頭」進場。
        # 為了效能，我們最多只要放 k 個列的頭進去就好，因為第 k+1 列以後的和絕對不可能是前 k 小。
        for i in range(min(k, len(nums1))):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))

        # 2. 補位邏輯
        res = []
        while h and len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])

            # 如果這一列還有「下一位」，就丟進去補位
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))

        return res




#把他想成m * n 的表格
#                nums2[0] = 2     nums2[1] = 4    nums2[2] = 6
#nums1[0] = 1       3(0,0)          5(0,1)          7(0,2)
#nums1[1] = 7       9(1,0)          11(1,1)         13(1,2)
#nums1[2] = 11      13(2,0)         15(2,1)         17(2,2)

#發現：每一橫列（Row）都是由小到大排好序的！
#algo: 我們不需要算出所有格子的值（那會是 O(M*N)，太大）。我們只需要用一個 Min-Heap 來管理每列的「排頭」

#存row or col都可 但會反應空間優化的敏感度
#如果 nums1 非常長，nums2 非常短：
    #存 Rows：Heap 裡面的代表會很多（跟著 nums1 走），Heap 會很大。
    #存 Cols：Heap 裡面的代表會很少（跟著 nums2 走），Heap 會很小。
#存 Rows 的時間複雜度是 O(klog(len(nums1)))
#存 Cols 的時間複雜度是 O(klog(len(nums2)))
#為了追求極致，我們可以在程式碼開頭加一個判斷：永遠讓 nums1 是比較短的那一個。這樣你的 Heap 永遠會維持在最小的狀態

#直覺選row是因為在電腦記憶體裡，二維陣列通常是 Row-major（按列儲存）