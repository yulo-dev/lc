class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #同一個 key 底下要收集「很多個字串」，所以 value 必須是一個「容器」來裝多個元素——最自然就是 list
        #不能用defaultdict(str) 因為str是不可變的 無法用append
        mapping = defaultdict(list)

        for ch in strs:
            key = "".join(sorted(ch))
            mapping[key].append(ch)

        return list(mapping.values())