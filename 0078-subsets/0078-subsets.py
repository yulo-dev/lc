class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        
        def backtrack(start):
            # 1. 每次進來都先存當前結果 (因為每個路徑過程都是一個合法子集)
            res.append(path.copy())
            
            # 2. 遍歷候選名單
            # for 迴圈是在做「橫向選擇」
            for i in range(start, len(nums)):
                # 選擇 (Choose)
                path.append(nums[i])
                
                # 探索 (Explore)：往下走，下一個開始的位置是 i + 1
                # backtrack(i + 1) 是在做「縱向深入」
                backtrack(i + 1)
                
                # 撤銷 (Unchoose)：回溯
                path.pop()
        
        backtrack(0)
        return res