class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        def vowel_replace(s):
            vowels = set("aeiou")
            output = []
            for ch in s:
                if ch in vowels:
                    output.append('*')
                else:
                    output.append(ch)
            return ''.join(output)

        exact_check = set(wordlist)
        lower_check = {}
        vowel_check = {}

        for ch in wordlist:
            lower_ch = ch.lower()

            if lower_ch not in lower_check:
                lower_check[lower_ch] = ch

            vowel_ch = vowel_replace(lower_ch)
            if vowel_ch not in vowel_check:
                vowel_check[vowel_ch] = ch

        res = []
        for ch in queries:
            lower_ch = ch.lower()

            if ch in exact_check:
                res.append(ch)
                continue
            if lower_ch in lower_check:
                res.append(lower_check[lower_ch])
                continue

            vowel_ch = vowel_replace(lower_ch)
            if vowel_ch in vowel_check:
                res.append(vowel_check[vowel_ch])
                continue

            res.append("")
        
        return res
            