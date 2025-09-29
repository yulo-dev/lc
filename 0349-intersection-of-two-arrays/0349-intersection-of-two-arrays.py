class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        res = []

        if len(set_1) > len(set_2):
            for val in set_1:
                if val in set_2:
                    res.append(val)
        else:
            for val in set_2:
                if val in set_1:
                    res.append(val)

        return res