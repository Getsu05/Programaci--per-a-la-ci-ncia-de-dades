"Mòdul per a l'Exercici 4: Partits guanyats a casa/fora."

import pandas as pd
import matplotlib.pyplot as plt


def FTR(data):
    "Calcula el nombre total de partits per tipus de resultat final."
    ftr_counts = data["FTR"].value_counts()
    ftr_df = ftr_counts.to_frame(name="Matches")
    ftr_df.index.name = "Result"
    return ftr_df.reindex(["H", "A", "D"])


def plot_FTR(ftr):
    "Representa gràficament el nombre de partits per cada tipus de resultat."
    plt.figure(figsize=(8, 5))
    colors = ["royalblue", "crimson", "orange"]
    plt.bar(ftr.index, ftr["Matches"], color=colors, edgecolor="black", alpha=0.8)
    plt.title("Distribució de Resultats Finals a LaLiga (1995-2025)", fontsize=14)
    plt.xlabel("Resultat (H: Casa, A: Fora, D: Empat)", fontsize=12)
    plt.ylabel("Nombre de Partits", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()