class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # L = first index where nums[i] >= target （left-most / lower_bound）
        # R = first index where nums[i] > target （right-most insertion / upper_bound）
        #
        #... < target | target target target | > target ...
        #                 L            R-1          R

        n = len(nums)
        if n == 0:
            return [-1, -1]

        def lower_bound(x: int) -> int:
            left = 0 
            right = n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= x:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def upper_bound(x: int) -> int:
            left = 0 
            right = n
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > x:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        l = lower_bound(target)

        # 必要檢查：
        # l == n 或是說 not (0 <= L < n)：插入點在最後面，代表 target 比全部都大 → 不存在（也避免越界）
        # nums[l] != target：插入點落在某個元素前，但那個元素不是 target → 不存在
        # 用 [5,7,7,8,8,10] target = 6 的例子去看
        if not (0 <= l < n) or nums[l] != target:
            return [-1, -1]

        r = upper_bound(target) - 1

        return [l, r]