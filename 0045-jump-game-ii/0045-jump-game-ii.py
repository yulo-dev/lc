class Solution:
    def jump(self, nums: List[int]) -> int:
        
        destination = len(nums) - 1
        steps = 0
        current_end = 0 #你「用目前這次跳數 steps」已經確定能到的最右邊界（本層邊界）
        farthest = 0 #「你在掃描本層所有可達位置後，推算出「如果再跳一步」能到的最右邊界（下一層候選邊界）

        for i in range(destination):  # 注意：不用走到最後一格
            
            farthest = max(farthest, i + nums[i])

            #當你掃到 i == current_end，代表：目前這一跳可達的所有位置都評估完了，必須多跳一次才能往更遠去。
            #沒有 current_end，你就不知道「什麼時候該 +1 跳」
            if i == current_end:      
                steps += 1
                current_end = farthest
                if current_end >=destination:
                    break

        return steps