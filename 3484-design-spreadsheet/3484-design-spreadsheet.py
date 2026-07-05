class Spreadsheet:

    def __init__(self, rows: int):
        self.cell_to_value = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.cell_to_value[cell] = value

    def resetCell(self, cell: str) -> None:
        self.cell_to_value[cell] = 0

    def getValue(self, formula: str) -> int:

        formula = formula[1:]        # 去掉 "="
        left, right = formula.split("+")
        
        def digit_or_alpha(var):
            if var[0] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"): # if var[0].isalpha() 也相同
                return self.cell_to_value[var] 
            else:
                return int(var)

        return digit_or_alpha(left) + digit_or_alpha(right)



# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)