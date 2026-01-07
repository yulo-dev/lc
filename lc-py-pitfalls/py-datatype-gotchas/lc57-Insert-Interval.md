
LC57 的 intervals 已排序且不重疊，所以最乾淨的流程是：

1. 把完全在 new 左邊的先放進 res
2. 合併所有與 new 重疊的
3. 放入合併後的 new
4. 把剩下右邊的全部放進 res


所以總結他的判斷：

1. end < new_start → 在左邊，直接放
2. start > new_end → 在右邊，要先插入 new（只插一次）再放它
3. else → 重疊，只更新 new_start/new_end


中間這個判斷式: 

Ｑ：哪時候不會執行裡面的 if not inserted: ？

Ａ：(1) newInterval 在最右邊（從來沒遇到右邊區間） (2) 你已經插過 newInterval 了（inserted=True）

```py
elif start > new_end:
  if not inserted:
    res.append([new_start, new_end])
    inserted = True
  res.append([start, end])
