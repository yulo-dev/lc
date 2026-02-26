class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # count: 紀錄 prefix_sum 出現的次數
        # 初始化 {0: 1} 是為了處理「從 index 0 開始就剛好等於 k」的情況
        # 如果不放這個，當第一個子陣列 [0...i] 總和剛好等於 k 時，current_sum - k 會等於 0，你會找不到它
        prefix_map = {0: 1}
        
        current_sum = 0
        result = 0
        
        for n in nums:
            current_sum += n  # 累加當前的前綴和
            
            # 找找看過去有沒有一個前綴和，剛好能跟現在湊成 k
            target = current_sum - k
            if target in prefix_map:
                result += prefix_map[target] # 到目前這一步之前，出現過哪些 prefix sum 
                                             # 所以不能先做 line22的+1 再存入res
            
            # 把當前的前綴和存入記帳本，供未來使用
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
            
        return result