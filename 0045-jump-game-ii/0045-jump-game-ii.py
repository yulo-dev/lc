class Solution:
    def jump(self, nums: List[int]) -> int:
        destination = len(nums) - 1
        farthest = 0 # within current layer, the farthest we can reach for next jump
        current_end = 0  # with 'steps' jumps, we can reach up to current_end
        steps = 0

        for i in range(destination):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                steps += 1
                current_end = farthest
                if farthest >= destination:
                    break

        return steps