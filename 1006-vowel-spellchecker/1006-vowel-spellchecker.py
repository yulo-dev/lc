class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # Define the helper that collapses vowels to a single placeholder.
        def devowel(s: str) -> str:
            vowels = set("aeiou")
            out = []
            for ch in s:
                # If the character is a vowel, I map it to '*', else keep it.
                out.append('*' if ch in vowels else ch)
            return ''.join(out)

        # 1) Exact set for O(1) exact-match checks.
        exact = set(wordlist) 
        # 2) Case-insensitive map: lowercased word -> first original word.
        case_map = {}  

        # 3) Vowel-error map: devoweled(lowercased word) -> first original word.
        vowel_map = {}  

        for w in wordlist:
            lw = w.lower()
            if lw not in case_map:
                case_map[lw] = w
            
            vw = devowel(lw)
            if vw not in vowel_map:
                vowel_map[vw] = w

        # Now I resolve each query using the defined priority.
        ans = []  
        for q in queries:
            # First priority: exact match — return the query itself.
            if q in exact:
                ans.append(q)  
                continue      

            # Second priority: case-insensitive match.
            lq = q.lower() 
            if lq in case_map:
                ans.append(case_map[lq]) 
                continue                 

            # Third priority: vowel-error match using the devoweled version.
            vq = devowel(lq) 
            if vq in vowel_map:
                ans.append(vowel_map[vq])  
                continue                   

            # If no rule matches, I return an empty string.
            ans.append("") 

        # Finally, I return the answers in the same order as the queries.
        return ans