1. `sorted vs sort`: sorted適用於任何iterable物件（str, list, tuple, set…）且不會改到原本的資料;sort只能用在list 且會原地排序 直接改動原本那個list
2. dict key 要不可變(immutable),所以要改成str or tuple, 所以這題key的排序的寫法 `''.join(sorted(s))` 或 `tuple(sorted(s))`。

## sort vs sorted

- `sorted(x)`：任何 **iterable** （str, list, tuple, set…）都能用，回傳 **新的 list** (不會改到原本的資料)
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



## One-glance Cheat Sheet 

**LC49 key 做法：**
- `key = ''.join(sorted(s))`  
- 或 `key = tuple(sorted(s))` 
- `groups = defaultdict(list)` 或 `mapping.setdefault(key, []).append(s)` 

**你要記的規則：**
- `sorted(x)` → 回傳 `list`
- `list` 不能當 dict key（not hashable）
- dict key 要 **hashable**（通常也要 immutable）

## Quick Compare Table

| Concept | 問題在問什麼 | 常見例子 | 跟 LC49 關係 |
|---|---|---|---|
| `sorted` vs `sort` | 用法/回傳/會不會改原物件 | `sorted(str)->list`；`list.sort()->None` | 用 `sorted(s)`，再轉 key |
| iterable | 能不能 `for x in obj` | `str/list/tuple/set/dict` | `s` 是 iterable 才能排序字元 |
| mutable | 能不能原地改內容 | list/dict/set  | 可變通常不能當 key |
| hashable | 能不能當 dict key/set 元素 | str/tuple/int  | key 必須 hashable（str/tuple） |
