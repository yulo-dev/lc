class Solution:
    def jump(self, nums: List[int]) -> int:
        
        destination = len(nums) - 1
        farthest = 0 # within current layer, the farthest we can reach for next jump
        current_end = 0  # with 'steps' jumps, we can reach up to current_end
        steps = 0

        for i in range(destination):
            farthest = max(farthest, i + nums[i])

            # When i reaches current_end, we have finished scanning all positions reachable with steps jumps. 
            # To go further, we must take one more jump, so steps++, and the new reachable boundary becomes farthest.
            if i == current_end:
                steps += 1
                current_end = farthest
                if current_end >= destination:
                    break

        return steps