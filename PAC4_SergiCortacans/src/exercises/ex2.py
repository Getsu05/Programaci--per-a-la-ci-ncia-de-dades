"Exercici 2: Partits totals jugats."

import pandas as pd
import matplotlib.pyplot as plt


def total_matches(data):
    "Calcula el nombre total de partits jugats per cada equip."
    home_counts = data["HomeTeam"].value_counts()
    away_counts = data["AwayTeam"].value_counts()
    total_counts = home_counts.add(away_counts, fill_value=0).astype(int)
    
    matches_team_total = total_counts.to_frame(name="Total_Matches")
    matches_team_total.index.name = "Team"
    return matches_team_total.sort_values(by="Total_Matches", ascending=False)


def plot_matches_team_total(matches_team_total):
    "Representa gràficament el nombre total de partits jugats per equip."
    plt.figure(figsize=(12, 6))
    plt.bar(
        matches_team_total.index,
        matches_team_total["Total_Matches"],
        color="skyblue",
        edgecolor="black"
    )
    plt.title("Nombre Total de Partits Jugats per Equip (1995-2025)", fontsize=14)
    plt.xlabel("Equips", fontsize=12)
    plt.ylabel("Número de Partits Total", fontsize=12)
    plt.xticks(rotation=90, fontsize=8)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()