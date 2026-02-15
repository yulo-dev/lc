class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        if n == 0:
            return [-1, -1]
        
        def find_leftmost():
            left = 0 
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1

            return left

        def find_rightmost():
            left = 0 
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1

            return left

        l = find_leftmost()

        #二分搜尋的 left 其實是一個「如果 target 存在，它應該出現的第一個位置」
        #所以需要 
        #1. 情況 A：Target 根本不在數組裡，但它有「應該在的位置」: 假設 nums = [1, 2, 4, 5]，你要找 target = 3，最後left 會停在索引 2（也就是數字 4 的位置）
        #2. 情況 B：Target 比數組裡所有的數都大: 假設 nums = [1, 2, 3]，你要找 target = 10，最後 left 會變成 3
        if not (0 <= l < n) or nums[l] != target:
            return [-1, -1]
            
        r = find_rightmost() - 1

        return [l, r]