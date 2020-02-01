import pandas as pd
import numpy as np

def join_sched_with_stats():
    # stats = pd.read_csv("Relevant_Data/merged_all.csv")
    stats = pd.DataFrame([["2020", "California", "lol"], ["2020", "Murray St", "hi"]], columns=['Season', 'Team', 'stat'])

    team0_cols = [col + " 0" for col in stats.columns]
    team0 = pd.DataFrame(stats.values, columns=team0_cols)

    team1_cols = [col + " 1" for col in stats.columns]
    team1 = pd.DataFrame(stats.values, columns=team1_cols)

    sched = pd.read_csv("Relevant_Data/RegularSeasonGames.csv")
    sched = sched.loc[:, sched.columns != "Unnamed: 0"]

    sched = pd.merge(sched, team0, left_on=["Season", "Team0"], right_on=["Season 0", "Team 0"])
    sched = pd.merge(sched, team1, left_on=["Season", "Team1"], right_on=["Season 1", "Team 1"])


    print(sched.head().to_string())

join_sched_with_stats()