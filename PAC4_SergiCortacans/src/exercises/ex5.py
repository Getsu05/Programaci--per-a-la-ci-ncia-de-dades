"Exercici 5: Classificació global 1995-2025."

import pandas as pd


def add_points(data):
    "Afegeix les columnes points_home i points_away al dataset."
    data["points_home"] = 0
    data["points_away"] = 0
    data.loc[data["FTR"] == "H", "points_home"] = 3
    data.loc[data["FTR"] == "A", "points_away"] = 3
    data.loc[data["FTR"] == "D", ["points_home", "points_away"]] = 1
    return data


def fun_total_points(data):
    "Calcula el total de punts aconseguits i acumulats per cada equip."
    home_pts = data.groupby("HomeTeam")["points_home"].sum()
    away_pts = data.groupby("AwayTeam")["points_away"].sum()
    total_series = home_pts.add(away_pts, fill_value=0).astype(int)
    total_series = total_series.sort_values(ascending=False)
    
    total_df = total_series.to_frame(name="Total_Points")
    total_df.index.name = "Team"
    return total_series, total_df


def alltime_winner(df_total_points):
    "Retorna el guanyador de la lliga històrica acumulada."
    return df_total_points.index[0]