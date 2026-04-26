import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])

    #df.drop_duplicates(subset=["欄位名稱"]) -> 移除重複 rows
    #df.drop_duplicates(subset=["col1", "col2"]) -> 如果根據多個欄位判斷重複