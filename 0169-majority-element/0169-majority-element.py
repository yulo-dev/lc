class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)

        for n in nums:
            cnt[n] += 1

        return max(cnt, key=cnt.get) 