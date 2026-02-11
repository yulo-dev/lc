class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 不能用set 因為set會佔用 O(n) space, 但題目要using only constant extra space

        # phase 1: find meeting point inside cycle
        #用0開頭, 把 0 當成「入口節點」（head）
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:  # pointers meet → cycle detected
                break

        # phase 2: find entrance (duplicate)
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break

        # When they meet again, it's the cycle entrance → duplicate number
        return slow