class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #1. get the mid from 1~max piles 
        #2. create a while loop: 
            #2a. create for loop: count the hours needed based on mid
            #2b. compare it with h
            #2c. move the pointers left or right
        #3. check the pointers and return result

        left = 1
        right = max(piles)

        while left + 1 < right:
            mid = left + (right - left) // 2  
            
            est = 0
            for p in piles:
                est += ceil(p / mid) 

            if est <= h:
                right = mid
            else:
                left = mid

        est = sum(ceil(p / left) for p in piles)
        if est <= h:
            return left
        return right

