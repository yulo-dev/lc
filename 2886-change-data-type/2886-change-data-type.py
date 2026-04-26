import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

    #df["column"] = df["column"].astype(型態)
    #.astype(int)      # 轉成整數
    #.astype(float)    # 轉成小數
    #.astype(str)      # 轉成字串