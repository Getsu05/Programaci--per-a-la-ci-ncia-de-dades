"Exercici 3: Distribució de gols."

import pandas as pd
import matplotlib.pyplot as plt


def goals_distribution(data):
    "Calcula la freqüència de partits segons els gols marcats."
    home_counts = data["FTHG"].value_counts().sort_index()
    distr_goals_home = home_counts.to_frame(name="Matches")
    distr_goals_home.index.name = "FTHG"

    away_counts = data["FTAG"].value_counts().sort_index()
    distr_goals_away = away_counts.to_frame(name="Matches")
    distr_goals_away.index.name = "FTAG"

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    "Representa en dues gràfiques de barres la distribució de gols."
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    axes[0].bar(distr_goals_home.index, distr_goals_home["Matches"], color="forestgreen", edgecolor="black", alpha=0.7)
    axes[0].set_title("Distribució Gols Casa (FTHG)")
    axes[0].set_xlabel("Gols Marcats")
    axes[0].set_ylabel("Número de Partits")
    axes[0].set_xticks(distr_goals_home.index)
    axes[0].grid(axis="y", linestyle="--", alpha=0.5)

    axes[1].bar(distr_goals_away.index, distr_goals_away["Matches"], color="crimson", edgecolor="black", alpha=0.7)
    axes[1].set_title("Distribució Gols Fora (FTAG)")
    axes[1].set_xlabel("Gols Marcats")
    axes[1].set_xticks(distr_goals_away.index)
    axes[1].grid(axis="y", linestyle="--", alpha=0.5)

    plt.suptitle("Freqüència de Partits segons els Gols Marcats (1995-2025)", fontsize=14)
    plt.tight_layout()