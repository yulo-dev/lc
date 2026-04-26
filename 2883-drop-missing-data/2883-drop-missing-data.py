import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])

    #只檢查 name 這一欄，如果 name 是空值，就把那一整列刪掉
    #df.dropna(subset=["欄位名稱"]) -> 根據某欄刪掉 missing rows
    #df.dropna(subset=["col1", "col2"]) -> 根據多個欄位檢查 missing