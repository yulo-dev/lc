class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            res = max(res, right - left + 1)

        return res


#解釋一下為什麼這題複雜度是Ｏ(n) 即便有for loop 跟 while loop

#The time complexity is O(n). The right pointer iterates through the string once, which is O(n). 
#For the while loop inside, although it looks like it could make this O(n²), 
#the left pointer can only move to the right and moves at most n steps in total across the entire algorithm. 
#So the total operations are at most 2n, which simplifies to O(n)."