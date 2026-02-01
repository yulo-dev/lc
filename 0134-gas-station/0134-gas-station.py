class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        #這一步先檢查到底有沒有可能走完
        #如果sum起來cost就一定會更多 那就不用跑下面了 直接給-1
        #同時這也很關鍵 如果我們檢查完確定 sum(gas) >= sum(cost) 代表一定繞得回來 等等一定有一個start可以辦到
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        #for loop 是在找 start（不是在模擬繞一圈）
        # sum(gas) >= sum(cost) 保證全局油量夠
        # greedy 找到的 start 保證從 start 到 n-1 不會爆
        # 那剩下繞回去的部分，靠「全局總和」+「你已經累積的油」一定能撐完
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0

        return start 