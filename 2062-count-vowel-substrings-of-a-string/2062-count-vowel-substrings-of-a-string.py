class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set("aeiou")
        res = 0

        for i in range(len(word)-1):
            vowels_appear = set()

            left = i
            right = i 

            while right < len(word):
                if word[right] not in vowels:
                    break

                vowels_appear.add(word[right])
                
                if len(vowels_appear) == 5:
                    res +=1

                right += 1

        return res