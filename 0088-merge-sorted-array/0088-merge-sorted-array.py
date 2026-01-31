class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1              # 指向 nums1 有效區最後
        j = n - 1              # 指向 nums2 最後
        write = m + n - 1      # 指向 nums1 最後一格（空位區）

        while j >= 0:          # nums2 需要全塞進去
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[write] = nums1[i]
                i -= 1
            else:
                nums1[write] = nums2[j]
                j -= 1
            write -= 1
