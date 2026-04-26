import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=["product"], var_name="quarter", value_name="sales")

# melt 就是把很多欄位「融化」成兩欄：
# 一欄放原本的 column name，一欄放原本的 value。

#df.melt(
#    id_vars=["保留不動的欄位"],
#    var_name="原本欄位名稱要變成的新欄名",
#    value_name="原本格子數值要變成的新欄名"
#)