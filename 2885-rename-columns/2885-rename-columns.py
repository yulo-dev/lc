import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns = {
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
        }
    )

    #rename(columns={...}) 是用來改欄位名稱
    #df.rename(columns={"舊欄位名稱": "新欄位名稱"}) 
    