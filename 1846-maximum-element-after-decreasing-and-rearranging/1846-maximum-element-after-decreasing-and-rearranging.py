class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        # sort it
        # for loop and check if the first number is equal or greater than 1
        # check the diff with the next number if the gap is greater than 1, decrease it to num + 1
        # after finish checking the array, we can get the greatest number in the array

        arr.sort() #1,1,2,2,2
        n = len(arr) - 1

        for i in range(len(arr)):
            if i == 0:
                if arr[i] >= 1:
                    arr[0] = 1
            else:
                if abs(arr[i] - arr[i-1]) > 1:
                    arr[i] = arr[i-1] + 1
                
        return arr[n]
