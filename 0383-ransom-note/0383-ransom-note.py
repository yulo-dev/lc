class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False

        ransomNote_cnt = Counter(ransomNote)
        magazine_cnt = Counter(magazine)

        for r in ransomNote_cnt:
            if r not in magazine_cnt or ransomNote_cnt[r] > magazine_cnt[r]:
                return False

        return True
