class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        
        arr.sort()
        min_gap = float("inf")
        res = []

        for i in range(1, len(arr)):
            gap = arr[i] - arr[i-1] 
            if gap < min_gap:
                min_gap = gap
                res = [[arr[i-1], arr[i]]]

            elif gap == min_gap:
                res.append([arr[i-1], arr[i]])


        return res




