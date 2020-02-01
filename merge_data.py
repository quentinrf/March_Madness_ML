import pandas as pd
import numpy as np
import os


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
        elif cols[i][0:13] == "School Totals":
            new_col = "School Totals " + str(stats.iloc[0, i])
        elif cols[i][0:15] == "Opponent Totals":
            new_col = "Opponent Totals " + str(stats.iloc[0, i])
        elif cols[i][0:15] == "School Advanced":
            new_col = "School Advanced " + str(stats.iloc[0, i])
        elif cols[i][0:17] == "Opponent Advanced":
            new_col = "Opponent Advanced " + str(stats.iloc[0, i])
        else:
            new_col = cols[i] + str(stats.iloc[0, i])

        new_cols.append(new_col)

    stats.columns = new_cols
    stats = stats.loc[:, stats.columns != "Rk"]
    stats = stats.loc[:, stats.columns != "nan"]
    stats = stats.loc[1:, :]
    return stats

def rename_cols_all():
    for stat_type in ["School", "Opponent", "AdvSchool", "AdvOpponent"]:
        for year in range(2010, 2021):
            data = pd.read_csv("Data/" + stat_type + "Stats/" + stat_type.lower() + "_" + str(year) + ".csv")
            data = rename_cols(data)
            data.to_csv("Processed_Data/" + stat_type + "Stats/" + stat_type.lower() + "_" + str(year) + ".csv")

def merge():
    for year in range(2010, 2021):
        merged = pd.read_csv("Processed_Data/SchoolStats/school_" + str(year) + ".csv")
        merged = merged.set_index('School')
        merged = merged.loc[:, merged.columns != "Unnamed: 0"]

        for stat_type in ["Opponent", "AdvSchool", "AdvOpponent"]:
            data = pd.read_csv("Processed_Data/" + stat_type + "Stats/" + stat_type.lower() + "_" + str(year) + ".csv")
            if stat_type[0:3] == "Adv":
                wanted_cols = pd.Series(data.columns).str.contains("Advanced")
            else:
                wanted_cols = pd.Series(data.columns).str.contains("Totals")
            school_col = pd.Series(data.columns == "School")
            data = data.loc[:, list(school_col | wanted_cols)]
            data = data.set_index('School')

            merged = merged.join(data)

        merged = merged.reset_index()
        merged.to_csv("Processed_Data/MergedStats/merged_" + str(year) + ".csv")


def merge_years():
    merged = pd.DataFrame()

    for year in range(2010, 2021):
        data = pd.read_csv("Processed_Data/MergedStats/merged_" + str(year) + ".csv")
        data = data.loc[:, data.columns != "Unnamed: 0"]
        cols = list(data.columns)
        cols.remove("School")
        data['Season'] = year
        data = data.loc[:, ['School', 'Season'] + list(cols)]

        merged = pd.concat([merged, data])
    merged = merged.reset_index(drop=True)

    merged.to_csv("Processed_Data/MergedStats/merged_all.csv")



merge_years()