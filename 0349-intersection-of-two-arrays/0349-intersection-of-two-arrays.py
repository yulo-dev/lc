class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        if len(set_1) > len(set_2):
            long = set_1
            short = set_2
        else:
            long = set_2
            short = set_1
        res = []

        for i in long:
            if i in short:
                res.append(i)
        return res