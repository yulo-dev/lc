class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = Counter(nums)

        h = []

        for num, freq in cnt.items(): #Counter(nums) 會把重複的合併成「唯一元素 → 次數」所以注意這邊在算複雜度 他走訪次數會比len(nums)小
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)

        return [num for (_, num) in h]

        #time: O(n + m log k) 
        #建 Counter 的時候，你必須看過 nums 的每個元素一次 → O(n)
        #建完 Counter 後，你只需要處理每個 unique 元素一次 → O(m log k)

        #space: O(m + k) 
        #Counter 存 m 個 key：O(m)
        #heap 最多 k 個：O(k)

        #Counter 建立時間是 O(n)（因為要掃過原始陣列每個元素一次）
        #Counter 佔用空間是 O(m)（因為只存 unique keys）
