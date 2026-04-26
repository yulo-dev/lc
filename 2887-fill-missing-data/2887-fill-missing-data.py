import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:

    #找到 quantity 這一欄裡面的空值，全部補成 0，再存回原本的 quantity 欄位
    products["quantity"] = products["quantity"].fillna(0)
    return products

    #補 missing value
    #df["column"] = df["column"].fillna(要補的值)