"Fitxer principal. Executa els diferents exercicis de la PAC."

import argparse
import os
import sys
import matplotlib.pyplot as plt

# Afegim el directori actual al path 
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importacions dels exercicis
from exercises import ex1, ex2, ex3, ex4, ex5, ex6, ex7


def run_incremental_analysis(max_exercise):
    "Executa els exercicis."
    ":param max_exercise: Enter (1-7) que indica fins a quin exercici executar."
    
    # Determinació de la ruta del fitxer de dades
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "data", "LaLiga_Matches.csv")

    # Control de seguretat bàsic
    if not os.path.exists(csv_path):
        print(f"No s'ha trobat el dataset a {csv_path}")
        return

    # Variables de persistència entre mòduls
    df_liga = None
    matches_team_total = None
    dataframe_total_points = None
    summary_1996_2025 = None

    # --- EXERCICI 1 ---
    if max_exercise >= 1:
        print("\n" + "="*60)
        print("=== EXERCICI 1: Càrrega del dataset i anàlisi exploratori ===")
        print("="*60)
        df_liga = ex1.load_and_eda(csv_path)
        print("\n--- Primers valors del dataset ---")
        print(df_liga.head())
        print("\n--- Últims valors del dataset ---")
        print(df_liga.tail())
        print("\n--- Informació general del dataset ---")
        df_liga.info()
        
        print("\nGenerant les gràfiques de distribució de gols (Boxplots)...")
        ex1.plot_home_away_goals(df_liga)
        plt.show()

    # --- EXERCICI 2 ---
    if max_exercise >= 2:
        print("\n" + "="*60)
        print("=== EXERCICI 2: Partits totals jugats ===")
        print("="*60)
        matches_team_total = ex2.total_matches(df_liga)
        print("\n--- Els 10 primers equips amb més partits ---")
        print(matches_team_total.head(10))

        max_matches = matches_team_total["Total_Matches"].max()
        always_first_div = matches_team_total[matches_team_total["Total_Matches"] == max_matches]
        print(f"\n--- Equips que sempre han estat a 1a Divisió (Partits: {max_matches}) ---")
        for team in always_first_div.index:
            print(f"- {team}")

        print("\nGenerant el gràfic de barres de partits totals per equip...")
        ex2.plot_matches_team_total(matches_team_total)
        plt.show()

    # --- EXERCICI 3 ---
    if max_exercise >= 3:
        print("\n" + "="*60)
        print("=== EXERCICI 3: Distribució de gols (Freqüències) ===")
        print("="*60)
        distr_home, distr_away = ex3.goals_distribution(df_liga)
        print("\n--- DataFrame Resultant: Gols Equip de Casa ---")
        print(distr_home)
        print("\n--- DataFrame Resultant: Gols Equip de Fora ---")
        print(distr_away)
        
        print("\nGenerant les gràfiques de distribució de freqüències...")
        ex3.plot_goals_distribution(distr_home, distr_away)
        plt.show()

    # --- EXERCICI 4 ---
    if max_exercise >= 4:
        print("\n" + "="*60)
        print("=== EXERCICI 4: Partits guanyats a casa/fora ===")
        print("="*60)
        dataframe_ftr = ex4.FTR(df_liga)
        print("\n--- DataFrame Resultant (ftr) ---")
        print(dataframe_ftr)

        total_matches_count = dataframe_ftr["Matches"].sum()
        home_wins = dataframe_ftr.loc["H", "Matches"]
        home_wins_percentage = (home_wins / total_matches_count) * 100
        print("\n--- Pregunta de reflexió ---")
        print(f"El percentatge de partits que guanyen els locals és del {home_wins_percentage:.2f}%.")

        print("\nGenerant la gràfica de barres de resultats finals...")
        ex4.plot_FTR(dataframe_ftr)
        plt.show()

    # --- EXERCICI 5 ---
    if max_exercise >= 5:
        print("\n" + "="*60)
        print("=== EXERCICI 5: Classificació global 1995-2025 ===")
        print("="*60)
        df_liga = ex5.add_points(df_liga)
        print("\n--- Columnes de punts afegides. Mostra dels 10 primers partits: ---")
        print(df_liga[["HomeTeam", "AwayTeam", "FTR", "points_home", "points_away"]].head(10))

        _, dataframe_total_points = ex5.fun_total_points(df_liga)
        print("\n--- Classificació històrica (Els 10 primers equips amb més punts) ---")
        print(dataframe_total_points.head(10))

        guanyador = ex5.alltime_winner(dataframe_total_points)
        print(f"\nEl guanyador d'aquesta lliga històrica i acumulada és el: {guanyador}")

    # --- EXERCICI 6 ---
    if max_exercise >= 6:
        print("\n" + "="*60)
        print("=== EXERCICI 6: Resum i Pòdium ===")
        print("="*60)
        h_goals, a_goals, t_goals = ex6.fun_total_goals(df_liga)
        print("\n--- Balanç Global de Gols ---")
        print(f"Gols Locals: {h_goals} | Gols Visitants: {a_goals} | Total Absolut: {t_goals}")

        df_h_goals, df_a_goals, df_t_goals = ex6.fun_total_goals_by_team(df_liga)
        print("\n--- Mètrica de Gols per Equip (Top 10 Gols Totals) ---")
        print(df_t_goals.head(10))

        summary_1996_2025 = ex6.fun_summary_1996_2025(
            dataframe_total_points, df_h_goals, df_a_goals, df_t_goals
        )
        print("\n--- Dataframe Unificat Resultant (summary_1996_2025) ---")
        print(summary_1996_2025.head(10))

        print("\nGenerant el gràfic de Pòdium amb els 3 millors equips històrics...")
        ex6.podium(summary_1996_2025)
        plt.show()

    # --- EXERCICI 7 ---
    if max_exercise >= 7:
        print("\n" + "="*60)
        print("=== EXERCICI 7: Graf de connexions (Top 5 Equips) ===")
        print("="*60)
        top_5_teams = list(dataframe_total_points.head(5).index)
        print(f"Els 5 equips seleccionats per al graf són: {top_5_teams}")

        print("\nGenerant el graf de xarxa amb NetworkX...")
        ex7.graf(df_liga, top_5_teams)
        plt.show()


if __name__ == "__main__":
    # Configuració del parser d'argparse demanat per la guia de la UOC
    parser = argparse.ArgumentParser(
        description="Script modularitzat per a l'anàlisi estadística històrica de LaLiga (PEC4)."
    )
    
    # Paràmetre d'execució incremental de tipus enter entre 1 i 7
    parser.add_argument(
        "-ex",
        type=int,
        choices=range(1, 8),
        default=7,
        help="Executa els exercicis de manera incremental fins al número especificat (ex: -ex 5 executa de l'1 al 5)."
    )

    args = parser.parse_args()
    
    # Trucada al motor incremental passant l'argument llegit
    run_incremental_analysis(args.ex)