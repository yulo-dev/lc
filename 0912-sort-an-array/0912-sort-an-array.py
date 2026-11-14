class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        
        #merge sort 
        def mergesort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])

            #Merge Sort 就是先一直切半、切半、切半，直到剩下一個元素，才開始執行 while 進行合併

            i = 0
            j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            #因為 i 和 j 指向的是「下一個還沒被加入 res 的元素」，而不是最後一個已經加入的元素。 所以要從 i、j 開始
            res.extend(left[i:])
            res.extend(right[j:])
            
            return res

        return mergesort(nums)

            