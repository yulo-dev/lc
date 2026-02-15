class TimeMap:

    def __init__(self):

        #Key-Value 需求 + 時間序列 (Time Series) = HashMap + Sorted List
        self.store = {} #key -> List of (timestamp, value)
        #也可寫成 self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] 
        self.store[key].append([timestamp, value])  
        #這題也可以把它存成tuple 因為代表他們是不可變的 這個timestamp對應這個value
        #且tuple跟list一樣支援binary search 以及 index 且題目說timestamp會遞增 所以這個tuple/list會天生保持有序
        #所以保持有序代表我可以直接做binary search 不用再排序一次才能做 所以能保持 O(log N)
        #且tuple比list省空間 所以其實更好
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # just reference, not copy, so not really slow, time complexity: O(1)
        # arr 就代表了那個存放 [timestamp, value] 的清單
        # 只查一次並存入變數，代碼會更高效且更好讀，不用每次呼叫key再去查
        arr = self.store[key]

        #Binary search: 一般的binary search
        left = 0
        right = len(arr) - 1
        res = ""

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1] # 暫時的答案
                left = mid + 1  # 試著往右找更大的 timestamp
            else:
                right = mid - 1

        return res
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)