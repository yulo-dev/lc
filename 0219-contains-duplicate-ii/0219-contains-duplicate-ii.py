class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        #dictionary只存一個數字「最近一次出現的 index」就夠了。
        #原因是：你在第 i 次看到值 x 時，要檢查的其實是i - last_index_of_x <= k。
        #而「最有可能成功」的一定是 離你最近的那次出現
        #所以這邊不需要想成一個數字的每個index都要存進去
        mapping = {}

        for i, n in enumerate(nums):
            if n in mapping and i - mapping[n] <= k:
                return True

            mapping[n] = i

        return False
        