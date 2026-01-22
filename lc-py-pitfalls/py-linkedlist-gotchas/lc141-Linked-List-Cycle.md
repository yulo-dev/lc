
寫 while fast and fast.next 的原因：

我們要避免的錯誤是：None.next（AttributeError）

fast.next.next 可以是 None, 只要 fast.next 不是 None，你就能「取到」fast.next.next 這個值（可能是節點，也可能是 None），不會 crash
所以重點是fast.next的時候不能是Ｎone, 但如果fast.next.next是None不會報錯
