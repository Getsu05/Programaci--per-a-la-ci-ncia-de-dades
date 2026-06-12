"Exercici 6: Dataframe summary i Pòdium."

import pandas as pd
import matplotlib.pyplot as plt


def fun_total_goals(data):
    "Retorna una tupla de tres enters amb els totals de gols."
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data):
    "Retorna una tupla de tres dataframes amb gols desglossats per equip."
    home_goals_by_team = data.groupby("HomeTeam")["FTHG"].sum().to_frame(name="Home_Goals")
    home_goals_by_team.index.name = "Team"

    away_goals_by_team = data.groupby("AwayTeam")["FTAG"].sum().to_frame(name="Away_Goals")
    away_goals_by_team.index.name = "Team"

    total_series = home_goals_by_team["Home_Goals"].add(away_goals_by_team["Away_Goals"], fill_value=0)
    total_goals_by_team = total_series.to_frame(name="Total_Goals").astype(int)
    total_goals_by_team.index.name = "Team"
    total_goals_by_team = total_goals_by_team.sort_values(by="Total_Goals", ascending=False)

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team):
    "Crea el dataframe unificat summary_1996_2025."
    if isinstance(total_points_by_team, pd.Series):
        total_points_by_team = total_points_by_team.to_frame(name="Total_Points")

    summary_df = pd.concat(
        [total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team],
        axis=1
    )
    return summary_df.sort_values(by="Total_Points", ascending=False)


def podium(summary_1996_2025):
    "Genera una gràfica amb estructura de pòdium sense eixos visibles."
    top_3 = summary_1996_2025.head(3)
    teams = list(top_3.index)
    points = list(top_3["Total_Points"])

    podium_teams = [teams[1], teams[0], teams[2]]
    podium_points = [points[1], points[0], points[2]]
    podium_positions = [2, 1, 3]

    x_coords = [1, 2, 3]
    colors = ["#C0C0C0", "#FFD700", "#CD7F32"]

    plt.figure(figsize=(8, 6))
    bars = plt.bar(x_coords, podium_points, color=colors, edgecolor="black", width=0.6)

    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height + (max(points) * 0.02),
                 f"{podium_teams[i]}", ha="center", va="bottom", fontsize=11, weight="bold")
        plt.text(bar.get_x() + bar.get_width() / 2.0, height / 2.0,
                 f"{podium_positions[i]}r", ha="center", va="center", fontsize=20, color="white", weight="bold")

    plt.title("Pòdium Històric de LaLiga (1995-2025)", fontsize=14, weight="bold", pad=20)
    plt.xlim(0.4, 3.6)
    plt.ylim(0, max(points) * 1.15)
    plt.axis("off")
    plt.tight_layout()