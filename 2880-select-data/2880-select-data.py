import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]

    #從 students 裡面，選出 student_id = 101 的那一列，然後只保留 name 和 age 兩欄。
    #df.loc[條件, [要回傳的欄位]]