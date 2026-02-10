class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)

        for ch, val in r_count.items():
            if (ch not in m_count) or (ch in m_count and m_count[ch] < r_count[ch]):
                return False
        return True
