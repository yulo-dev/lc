class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        farthest = 0
        for i in range(len(nums)):
            #如果 i > farthest，代表你連 i 這格都到不了，那後面也不用看了 → False
            if i > farthest:
                return False

            #要 i 還在陰影裡（i ≤ farthest），我就用它當跳板去更新 farthest（擴張陰影）
            farthest = max(farthest, i + nums[i])

        return True


#那為什麼 [3,2,1,0,4] 這例子真的「永遠擴張不了」？
#關鍵是：所有能到的跳板 i 都只能到 3。
#i=0 → reach=3
#i=1 → reach=3
#i=2 → reach=3
#i=3 → reach=3
#對於所有「你站得到的 i」（0~3），它們的最遠落點都 ≤ 3。
#所以陰影的右邊界 farthest 永遠卡在 3，根本沒有任何一步可以把它推到 4。
#所以當你掃到 i=4 時才說 False，是因為：
#你已經把 所有可能擴張陰影的跳板（0..3） 都檢查完了
#沒有任何一個能把 farthest > 3
#那 i=4 不可能到達