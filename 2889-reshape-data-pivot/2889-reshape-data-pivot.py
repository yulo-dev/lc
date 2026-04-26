import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month", columns="city", values="temperature")

    # df.pivot(
    # index="誰當 row",
    # columns="誰變成 column",
    # values="格子裡放什麼值"
    # )