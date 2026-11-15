class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()

        left = 0
        right = len(people) - 1

        res = 0

        while left <= right:
            tot = people[left] + people[right]
            if tot <= limit:
                res += 1
                left += 1
                right -= 1
            else:
                res += 1
                right -= 1

        return res