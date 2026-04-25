import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

    #.shape 回傳 (行數, 列數)，用 list() 轉成 list。