class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        #注意
        #它們要表示「找不到更小的邊界」時的 哨兵值
        #而且這個哨兵值會直接影響寬度公式 width = rightLess[i] - leftLess[i] - 1
        #leftLess[i] 表示：i 左邊第一個 更小 的 index, 如果左邊根本沒有更小的（i 是目前最小/並列最小
        #那左邊界就應該視為「在陣列外面」：i=0
        left_less = [-1] * n

        #rightLess[i] 表示：i 右邊第一個 更小 的 index。
        #如果右邊沒有更小的，就應該視為「在最右邊外面」：→ 等於能延伸到最右端
        right_less = [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left_less[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right_less[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            #left_less[i] 和 right_less[i] 指的是「第一個更小柱子的 index」
            #那兩根更小的柱子本身 不能包含在矩形寬度裡，所以中間能用的柱子數量要把兩邊各排除掉, 結果就會多出這個 -1
            width = right_less[i] - left_less[i] - 1
            ans = max(ans, width * heights[i])

        return ans
