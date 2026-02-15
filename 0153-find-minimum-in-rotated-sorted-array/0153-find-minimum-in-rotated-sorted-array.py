class Solution:
    def findMin(self, nums: List[int]) -> int:
        #關鍵在他需要跟nums[right]比較 才能判斷出旋轉
        #因為「沒旋轉」和「有旋轉」的情況下，跟左邊比的結果是一樣的，但跟右邊比，這兩種情況的結果是相反的，這才能產生判斷訊號
        #他是用exact value的模板去做微調

        left, right = 0, len(nums) - 1


        #注意：這裡用 < 而不是 <=，因為我們要找的是「那一個點」，
        #當 left == right 時，那個點就是唯一答案。
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1 # 說明 mid 在左邊的高坡，最小值在右邊，且不可能是 mid
            else:
                right = mid # 說明 mid 在右邊的低坡，mid 可能是最小值，這裡不能 mid - 1，因為 mid 可能是答案
                
        return nums[left]