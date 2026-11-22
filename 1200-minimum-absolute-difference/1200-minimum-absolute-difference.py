class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        
        #[1,2,3,4]
        #[1]: (1,2), (2,3), (3,4)
        #return dict.values() 

        arr.sort()
        gap_from = defaultdict(list)

        for i in range(1, len(arr)):
            gap = arr[i] - arr[i-1] 
            gap_from[gap].append([arr[i-1],arr[i]])

        min_gap = float("inf")

        for gap, res in gap_from.items():
            min_gap = min(gap, min_gap)

        #min_gap = min(gap_from) 也可以

        return gap_from[min_gap]




