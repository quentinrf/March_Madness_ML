import pandas as pd


def rename_cols(stats):

    cols = list(stats.columns)
    new_cols = []

    for i in range(len(cols)):
        if cols[i][0:9] == "Unnamed: ":
            new_col = str(stats.iloc[0, i])
        elif cols[i][0:7] == "Overall":
            new_col = "Overall " + str(stats.iloc[0, i])
        elif cols[i][0:5] == "Conf.":
            new_col = "Conf. " + str(stats.iloc[0, i])
        elif cols[i][0:4] == "Home":
            new_col = "Home " + str(stats.iloc[0, i])
        elif cols[i][0:4] == "Away":
            new_col = "Away " + str(stats.iloc[0, i])
        elif cols[i][0:6] == "Points":
            new_col = "Points " + str(stats.iloc[0, i])
        elif cols[i][0:15] == "Opponent Totals":
            new_col = "Opponent Totals " + str(stats.iloc[0, i])
        else:
            new_col = cols[i] + str(stats.iloc[0, i])

        new_cols.append(new_col)

    stats.columns = new_cols
    stats = stats.loc[:, stats.columns != "Rk"]
    stats = stats.loc[:, stats.columns != "nan"]
    stats = stats.loc[1:, :]







def main():
    stats = pd.read_csv("OpponentStats/opponent_2020.csv")
    rename_cols(stats)
main()