class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7
        # 1. 為了「一排一排賣」，我們改用排序，並補一個 0 當作地板
        inventory.sort(reverse=True)
        inventory.append(0)
        
        res = 0
        width = 1 # 這相當於 Heap 中「價值相同且最高」的球種數量
        
        for i in range(len(inventory) - 1):
            # 計算目前的「高度差」
            diff = inventory[i] - inventory[i+1]
            
            # Ａ：如果這「一整橫排」的球夠付剩下的訂單
            # width * diff 就是這一層「凸出來」的部分總共有多少顆球
            if width * diff <= orders:
                # --- 這一步 = 你的 while 跑了 width * diff 次 ---
                top = inventory[i]
                bottom = inventory[i+1]

                # 使用等差數列：(首項 + 末項) * 項數 / 2
                # 這裡每一種顏色賣掉的總和是 (top + ... + bottom + 1)
                # 為什麼要 +1？ 因為我們這一波只賣到 bottom 的上一層
                num_terms = diff
                sum_per_color = (top + bottom + 1) * num_terms // 2
                res = (res + width * sum_per_color) % MOD
                
                orders -= width * diff
                width += 1 # 寬度增加，就像 Heap 裡現在有更多種球價值並列最高


            # B: 客人要的球沒那麼多，我如果把這層全削掉，就賣過頭了
            else:
                # --- 這一步 = 剩下的訂單不夠賣一整排了 ---
                each_color_sell = orders // width
                remainder = orders % width
                
                top = inventory[i]
                bottom = top - each_color_sell
                
                # 1. 先處理整齊的部分
                res = (res + width * (top + bottom + 1) * each_color_sell // 2) % MOD
                # 2. 處理剩下的餘數，利潤就是現在的底價
                res = (res + remainder * bottom) % MOD
                
                orders = 0
                break
                
        return res


#貪婪：一排一排賣