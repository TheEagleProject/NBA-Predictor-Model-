import pandas as pd
df = pd.read_csv("nba_games.csv", index_col=0)

df = df.sort_values("date")
df = df.reset_index(drop=True)

del df["mp1"]
del df["mp_opp.1"]
del df["index_opp"]

def add_target(team):
    team["target"] = team["won"].shift(-1)
    return team

df = df.groupby("team", group_keys=False).apply(add_target)

df["target"] [pd.isnull(df["target"])] = 2
df["target"] = df["target"].astype(int, errors="ignore")

nulls = pd.isnull(df)
nulls = nulls.sum()
nulls[nulls > 0]
valid_column = df.columns[~df.clumns.isin(nulls.index)]