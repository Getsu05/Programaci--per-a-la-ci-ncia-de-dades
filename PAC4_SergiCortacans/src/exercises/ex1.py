"Exercici 1: Càrrega i exploració inicial."

import pandas as pd
import matplotlib.pyplot as plt


def load_and_eda(file_path):
    "Carrega el dataset i elimina columnes de la mitja part."
    df = pd.read_csv(file_path)
    columns_to_drop = ["HTHG", "HTAG", "HTR"]
    df = df.drop(columns=columns_to_drop, errors="ignore")
    return df


def plot_home_away_goals(data):
    "Genera la figura de boxplots de la distribució de gols."
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)
    axes[0].boxplot(data["FTHG"].dropna())
    axes[0].set_title("Gols Equip de Casa (FTHG)")
    axes[0].set_ylabel("Nombre de Gols")
    axes[0].grid(True, linestyle="--", alpha=0.7)

    axes[1].boxplot(data["FTAG"].dropna())
    axes[1].set_title("Gols Equip de Fora (FTAG)")
    axes[1].grid(True, linestyle="--", alpha=0.7)
    
    plt.suptitle("Distribució de Gols a LaLiga (1995-2025)", fontsize=14)
    plt.tight_layout()