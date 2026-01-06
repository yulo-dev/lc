
1.dict的key要是不可變 hashable/immutable , 所以在create key的時候使用的sorting 就要用sorted 不能用sort, 因為sort只能用在list, 但list是not hashable

1.1. key 要 hashable（通常也意味著 immutable）；hashable 通常是 immutable；immutable 不一定 hashable（例如含 list 的 tuple）

2.注意sorted vs sort: sorted適用於任何iterable物件（str, list, tuple, set…）且不會改到原本的資料;sort只能用在list 且會原地排序 直接改動原本那個list

3. dictionary 要用defaultdict先建立 不然這段會出：KeyError（第一次 mapping[key] 還不存在就 .append）; 前面先做出key沒錯 但他只是一個變數, 在dictionary裡面還沒有這個entry 所以dict裡面的key並不存在

![img](../images/lc49-1.png)




## sort vs sorted

https://www.geeksforgeeks.org/python/python-difference-between-sorted-and-sort/

- `sorted(x)`：任何 **iterable** （str, list, tuple, set…）都能用，回傳 **新的 list** (不會改到原本的資料) 注意！sorted() 的設計就是：不管你丟進去是什麼 iterable，它一律回傳「新的 list」
- `list.sort()`：只能用在 **list**，**原地改動**，回傳 `None`
- **LC49**：`s` 是 `str` → 用 `sorted(s)`，再轉成可當 key 的型別（`str` 或 `tuple`）



## iterable vs non-iterable

- **iterable**：能被 `for ... in ...` 走過  
  例：`str / list / tuple / set / dict / range`
- **non-iterable**：不能直接被 `for` 迭代  
  例：`int`
- **LC49**：字串是 iterable，所以 `sorted(s)` 才能把字元拿出來排序


## immutable vs mutable

- **immutable**：內容不能改  
  例：`str / tuple / int`
- **mutable**：內容可改  
  例：`list / dict / set`
- **LC49**：你要的 `key` 最好是 immutable（因為通常才能 hash）


## hashable vs not hashable

- **hashable**：可以當 `dict` key / 放進 `set`  
  例：`str / tuple / int / frozenset`
- **not hashable**：不能當 key  
  例：`list / dict / set`
- **LC49**：`sorted(s)` 產生的是 `list` → 不 hashable，所以要轉成 `str` 或 `tuple`
  - `''.join(sorted(s))` 
  - `tuple(sorted(s))` 

--> immutable 是「不能改」；hashable 是「能當 key」；要能當 key，通常就得不能改。


