

先把「左邊乘積」塞進 res, 再把「右邊乘積」乘回去


針對裡面的程式：
1. 先寫答案，再更新狀態
2. res[i] 放的是「不包含自己」：所以要先用舊的 prefix/postfix

```py
res[i] = prefix
prefix *= nums[i]
