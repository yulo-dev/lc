class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res) #subset不在主程式定義 因為他會一直變動
        return res

    def dfs(self, nums, k, subset, res):
        #不選
        res.append(subset[:])

        #選
        for i in range(k, len(nums)):
            #選完加上去
            subset.append(nums[i])
            #繼續往下看選或不選
            self.dfs(nums, i+1, subset, res)
            #最深的走到底了 一個一個回頭
            subset.pop()


# 時間複雜度：O(n⋅2^n) 因為 #line 9 複製成本 n 然後整個選或不選導致有 2^n 個子集, n是len(nums)
# space 也相同 O(n⋅2^n)  因為輸出本身有 2^n 個子集，每個子集最多長度 n, 這邊call stack O(n)可忽略