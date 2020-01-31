import pandas as pd

stats = pd.read_csv("OpponentStats/opponent_2020.csv")
stats.columns = stats.loc[0, :]

print(stats.loc[0:, :].to_string())