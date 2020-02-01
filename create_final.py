import pandas as pd
import numpy as np

def join_sched_with_stats():
    stats = pd.read_csv("Relevant_Data/merged_all_kaggle_mapped.csv")
    stats['Season_School'] = stats['Season'].astype(str) + stats['School']
    stats_cols = ['Season_School'] + list(stats.columns)[2:-1]
    stats = stats.loc[:, stats_cols]

    team0_cols = [col + " 0" for col in stats.columns]
    team0 = pd.DataFrame(stats.values, columns=team0_cols)
    team0_cols.remove('Season_School 0')

    team1_cols = [col + " 1" for col in stats.columns]
    team1 = pd.DataFrame(stats.values, columns=team1_cols)
    team1_cols.remove('Season_School 1')

    sched = pd.read_csv("Relevant_Data/RegularSeasonGames.csv")
    sched = sched.loc[:, sched.columns != "Unnamed: 0"]
    sched['Season_Team0'] = sched['Season'].astype(str) + sched['Team0']
    sched['Season_Team1'] = sched['Season'].astype(str) + sched['Team1']

    sched = sched.merge(team0, left_on='Season_Team0', right_on="Season_School 0")
    sched = sched.merge(team1, left_on='Season_Team1', right_on="Season_School 1")
    sched = sched.loc[:, ['Season', 'Team0'] + list(team0_cols) + ['Team1'] + list(team1_cols) + ['Winner']]

    sched.to_csv("Relevant_Data/final.csv", index=False)

# join_sched_with_stats()