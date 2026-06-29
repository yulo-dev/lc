class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        #for loop the patterns and use another for loop to check
        #whether the pattern is in the word

        res = 0

        for p in patterns:
            if p in word:
                res += 1
        return res