"""Mòdul d'utilitats per a l'anàlisi de dades històriques de LaLiga.

Aquest mòdul conté les funcions de càrrega, anàlisi exploratori (EDA)
i visualització gràfica de les dades del campionat.
"""

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def load_and_eda(file_path):
    """Carrega el dataset, elimina columnes de la mitja part i fa un EDA bàsic.

    Elimina les columnes 'HTHG', 'HTAG' i 'HTR'. Mostra per pantalla els
    primers i últims valors, així com la informació general del DataFrame.

    :param file_path: Ruta del fitxer CSV.
    :return: DataFrame de pandas netejat.
    """
    # Carrega del dataset
    df = pd.read_csv(file_path)

    # Eliminar les columnes especificades
    columns_to_drop = ["HTHG", "HTAG", "HTR"]
    df = df.drop(columns=columns_to_drop, errors="ignore")

    # Mostrar els primers i últims valors
    print("\n--- Primers valors del dataset ---")
    print(df.head())

    print("\n--- Últims valors del dataset ---")
    print(df.tail())

    # Informació rellevant del dataset
    print("\n--- Informació general del dataset ---")
    df.info()

    return df


def plot_home_away_goals(data):
    """Mostra una figura amb dos boxplots per veure la distribució de gols.

    Compara la distribució de gols marcats pels equips de casa (FTHG)
    i els equips de fora (FTAG).

    :param data: DataFrame de pandas amb les dades de LaLiga.
    """
    # Creem una figura amb dos subplots (1 fila, 2 columnes)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

    # Boxplot per als gols de l'equip de casa
    axes[0].boxplot(data["FTHG"].dropna())
    axes[0].set_title("Gols Equip de Casa (FTHG)")
    axes[0].set_ylabel("Nombre de Gols")
    axes[0].grid(True, linestyle="--", alpha=0.7)

    # Boxplot per als gols de l'equip de fora
    axes[1].boxplot(data["FTAG"].dropna())
    axes[1].set_title("Gols Equip de Fora (FTAG)")
    axes[1].grid(True, linestyle="--", alpha=0.7)

    # Ajustar l'estructura i mostrar la gràfica
    plt.suptitle("Distribució de Gols a LaLiga (1995-2025)", fontsize=14)
    plt.tight_layout()
    plt.show()

def total_matches(data):
    """Calcula el nombre total de partits jugats per cada equip (casa + fora).

    :param data: DataFrame de pandas amb les dades de LaLiga.
    :return: DataFrame ordenat descendentment amb la columna 'Total_Matches'.
    """
    # Comptem quants partits ha jugat cada equip com a local i com a visitant
    home_counts = data["HomeTeam"].value_counts()
    away_counts = data["AwayTeam"].value_counts()

    # Sumem ambdues sèries alineant els equips (omplint amb 0 si un equip no té partits)
    total_counts = home_counts.add(away_counts, fill_value=0).astype(int)

    # Convertim la sèrie en un DataFrame i l'ordenem de més a menys partits
    matches_team_total = total_counts.to_frame(name="Total_Matches")
    matches_team_total.index.name = "Team"
    matches_team_total = matches_team_total.sort_values(
        by="Total_Matches", ascending=False
    )

    return matches_team_total


def plot_matches_team_total(matches_team_total):
    """Representa gràficament el nombre total de partits jugats per cada equip.

    :param matches_team_total: DataFrame amb els totals per equip.
    """
    plt.figure(figsize=(12, 6))

    # Creem un gràfic de barres
    plt.bar(
        matches_team_total.index,
        matches_team_total["Total_Matches"],
        color="skyblue",
        edgecolor="black",
    )

    # Configuració de l'estètica del gràfic
    plt.title("Nombre Total de Partits Jugats per Equip (1995-2025)", fontsize=14)
    plt.xlabel("Equips", fontsize=12)
    plt.ylabel("Número de Partits Total", fontsize=12)
    plt.xticks(rotation=90, fontsize=8)  # Rotem els noms dels equips per llegir-los bé
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()

def goals_distribution(data):
    """Calcula la freqüència de partits segons els gols marcats a casa i fora.

    :param data: DataFrame de pandas amb les dades de LaLiga.
    :return: Una tupla amb dos DataFrames (distr_goals_home, distr_goals_away).
    """
    # Comptem quants partits hi ha per cada quantitat de gols a casa
    home_counts = data["FTHG"].value_counts().sort_index()
    distr_goals_home = home_counts.to_frame(name="Matches")
    distr_goals_home.index.name = "FTHG"

    # Comptem quants partits hi ha per cada quantitat de gols a fora
    away_counts = data["FTAG"].value_counts().sort_index()
    distr_goals_away = away_counts.to_frame(name="Matches")
    distr_goals_away.index.name = "FTAG"

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    """Representa en dues gràfiques de barres la distribució de gols.

    :param distr_goals_home: Freqüències de gols de l'equip de casa.
    :param distr_goals_away: Freqüències de gols de l'equip de fora.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    # Gràfic per a l'equip de casa
    axes[0].bar(
        distr_goals_home.index,
        distr_goals_home["Matches"],
        color="forestgreen",
        edgecolor="black",
        alpha=0.7,
    )
    axes[0].set_title("Distribució Gols Casa (FTHG)")
    axes[0].set_xlabel("Gols Marcats")
    axes[0].set_ylabel("Número de Partits")
    axes[0].set_xticks(distr_goals_home.index)
    axes[0].grid(axis="y", linestyle="--", alpha=0.5)

    # Gràfic per a l'equip de fora
    axes[1].bar(
        distr_goals_away.index,
        distr_goals_away["Matches"],
        color="crimson",
        edgecolor="black",
        alpha=0.7,
    )
    axes[1].set_title("Distribució Gols Fora (FTAG)")
    axes[1].set_xlabel("Gols Marcats")
    axes[1].set_xticks(distr_goals_away.index)
    axes[1].grid(axis="y", linestyle="--", alpha=0.5)

    plt.suptitle(
        "Freqüència de Partits segons els Gols Marcats (1995-2025)", fontsize=14
    )
    plt.tight_layout()
    plt.show()

def FTR(data):
    """Calcula el nombre total de partits guanyats a casa, a fora o empatats.

    :param data: DataFrame de pandas amb les dades de LaLiga.
    :return: DataFrame amb l'índex (H, A, D) i la columna 'Matches'.
    """
    # Comptem les freqüències dels valors de la columna FTR
    ftr_counts = data["FTR"].value_counts()

    # Convertim la sèrie en un DataFrame net
    ftr_df = ftr_counts.to_frame(name="Matches")
    ftr_df.index.name = "Result"

    # Ens assegurem que l'ordre sigui l'especificat (H, A, D) per si de cas
    # Reindexem per evitar canvis d'ordre segons el volum de dades
    ftr_df = ftr_df.reindex(["H", "A", "D"])

    return ftr_df


def plot_FTR(ftr):
    """Representa gràficament el nombre de partits per cada tipus de resultat.

    :param ftr: DataFrame amb les freqüències de cada resultat (H, A, D).
    """
    plt.figure(figsize=(8, 5))

    # Creem el gràfic de barres
    colors = ["royalblue", "crimson", "orange"]
    plt.bar(ftr.index, ftr["Matches"], color=colors, edgecolor="black", alpha=0.8)

    # Configuració de l'estètica
    plt.title("Distribució de Resultats Finals a LaLiga (1995-2025)", fontsize=14)
    plt.xlabel("Resultat (H: Casa, A: Fora, D: Empat)", fontsize=12)
    plt.ylabel("Nombre de Partits", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

def add_points(data):
    """Afegeix les columnes 'points_home' i 'points_away' al dataset segons el resultat.

    Guanyador local (H): 3 punts a casa, 0 fora.
    Guanyador visitant (A): 0 punts a casa, 3 fora.
    Empat (D): 1 punt a casa, 1 punt fora.

    :param data: DataFrame original de LaLiga.
    :return: DataFrame modificat amb les noves columnes de punts.
    """
    # Inicialitzem les columnes a 0
    data["points_home"] = 0
    data["points_away"] = 0

    # Apliquem les condicions segons la columna FTR
    data.loc[data["FTR"] == "H", "points_home"] = 3
    data.loc[data["FTR"] == "A", "points_away"] = 3

    data.loc[data["FTR"] == "D", ["points_home", "points_away"]] = 1

    return data


def fun_total_points(data):
    """Calcula el total de punts acumulats des de 1995 per a cada equip.

    :param data: DataFrame de LaLiga amb les columnes de punts ja calculades.
    :return: Una tupla amb (Series de punts totals, DataFrame de punts totals).
    """
    # Agrupem els punts aconseguits a casa per cada equip
    home_pts = data.groupby("HomeTeam")["points_home"].sum()

    # Agrupem els punts aconseguits a fora per cada equip
    away_pts = data.groupby("AwayTeam")["points_away"].sum()

    # Sumem els punts de casa i fora alineant els equips
    total_series = home_pts.add(away_pts, fill_value=0).astype(int)

    # Ordenem la sèrie de més a menys punts
    total_series = total_series.sort_values(ascending=False)

    # Convertim la Sèrie a un DataFrame formal per complir la proposta de retorn
    total_df = total_series.to_frame(name="Total_Points")
    total_df.index.name = "Team"

    return total_series, total_df


def alltime_winner(df_total_points):
    """Retorna el nom de l'equip que ha acumulat més punts històricament.

    :param df_total_points: DataFrame ordenat amb la classificació històrica.
    :return: Cadena de text (str) amb el nom de l'equip guanyador.
    """
    # Com que el DataFrame està ordenat descendentment, el primer element (.index[0]) és el líder
    winner = df_total_points.index[0]
    return winner

def fun_total_goals(data):
    """Calcula el sumatori de gols a casa, a fora i el total absolut.

    :param data: DataFrame original de LaLiga.
    :return: Tupla amb tres enters (home_goals, away_goals, total_goals).
    """
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals
    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data):
    """Calcula els gols fets a casa, a fora i totals per cada equip.

    :param data: DataFrame original de LaLiga.
    :return: Tupla de tres DataFrames (home_goals_by_team, away_goals_by_team,
             total_goals_by_team).
    """
    # Gols marcats com a local agrupats per equip
    home_goals_by_team = data.groupby("HomeTeam")["FTHG"].sum().to_frame(name="Home_Goals")
    home_goals_by_team.index.name = "Team"

    # Gols marcats com a visitant agrupats per equip
    away_goals_by_team = data.groupby("AwayTeam")["FTAG"].sum().to_frame(name="Away_Goals")
    away_goals_by_team.index.name = "Team"

    # Sumem ambdós per obtenir els gols totals
    total_series = home_goals_by_team["Home_Goals"].add(away_goals_by_team["Away_Goals"], fill_value=0)
    total_goals_by_team = total_series.to_frame(name="Total_Goals").astype(int)
    total_goals_by_team.index.name = "Team"
    total_goals_by_team = total_goals_by_team.sort_values(by="Total_Goals", ascending=False)

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team):
    """Concatena horitzontalment les mètriques històriques calculades dels equips.

    :param total_points_by_team: DataFrame o Sèrie amb els punts totals.
    :param home_goals_by_team: DataFrame amb gols a casa.
    :param away_goals_by_team: DataFrame amb gols a fora.
    :param total_goals_by_team: DataFrame amb gols totals.
    :return: DataFrame unificat 'summary_1996_2025' ordenat per punts de forma descendent.
    """
    # Convertim a DataFrame si algun argument ens arriba com a Sèrie per assegurar la consistència
    if isinstance(total_points_by_team, pd.Series):
        total_points_by_team = total_points_by_team.to_frame(name="Total_Points")

    # Concatenem les columnes utilitzant l'índex (nom de l'equip) com a nexe d'unió
    summary_df = pd.concat(
        [total_points_by_team, home_goals_by_team, away_goals_by_team, total_goals_by_team],
        axis=1
    )
    
    # Ordenem la classificació final per punts aconseguits
    summary_df = summary_df.sort_values(by="Total_Points", ascending=False)
    return summary_df


def podium(summary_1996_2025):
    """Genera una gràfica de barres personalitzada amb estructura de pòdium (2n, 1r, 3r).

    :param summary_1996_2025: DataFrame unificat i ordenat de la classificació.
    """
    # Extraiem els tres primers equips (el pòdium)
    top_3 = summary_1996_2025.head(3)
    teams = list(top_3.index)
    points = list(top_3["Total_Points"])

    # Reordenem les posicions per fer l'efecte visual de pòdium de competició: [Segon, Primer, Tercer]
    podium_teams = [teams[1], teams[0], teams[2]]
    podium_points = [points[1], points[0], points[2]]
    podium_positions = [2, 1, 3]  # Posicions numèriques reals per ordenar el text

    # Definim les coordenades X de les tres barres fixes al gràfic
    x_coords = [1, 2, 3]
    colors = ["#C0C0C0", "#FFD700", "#CD7F32"]  # Argent (2n), Or (1r), Bronze (3r)

    plt.figure(figsize=(8, 6))
    bars = plt.bar(x_coords, podium_points, color=colors, edgecolor="black", width=0.6)

    # Afegim el text del nom de l'equip i la posició sobre/dins de cada barra
    for i, bar in enumerate(bars):
        height = bar.get_height()
        
        # Nom de l'equip a sobre de la barra
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height + (max(points) * 0.02),
            f"{podium_teams[i]}",
            ha="center",
            va="bottom",
            fontsize=12,
            weight="bold"
        )
        
        # Posició del pòdium (1r, 2n, 3r) inscrita a l'interior de la barra
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height / 2.0,
            f"{podium_positions[i]}r",
            ha="center",
            va="center",
            fontsize=20,
            color="white",
            weight="bold"
        )

    # Configuració d'estil estricta demanada per l'enunciat (sense etiquetes de l'eix)
    plt.title("Pòdium Històric de LaLiga (1995-2025)", fontsize=14, weight="bold", pad=20)
    plt.xlim(0.4, 3.6)
    plt.ylim(0, max(points) * 1.15)  # Donem marge superior perquè es llegeixin bé els noms
    plt.axis("off")  # Desactiva completament els eixos i etiquetes tal com demana l'enunciat

    plt.tight_layout()
    plt.show()

def graf(data, selected_teams):
    """Genera i dibuixa un graf de connexions (partits jugats) entre els equips seleccionats.

    Filtra els partits on tant l'equip local com el visitant formen part del Top 5,
    compta quants cops s'han enfrontat i en dibuixa un graf no dirigit amb els totals.

    :param data: DataFrame original de LaLiga.
    :param selected_teams: Llista o índex amb els noms dels 5 millors equips.
    """
    # 1. Filtrar el dataset: tant HomeTeam com AwayTeam han d'estar al Top 5
    filtered_df = data[
        data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)
    ].copy()

    # 2. Comptar els enfrontaments totals entre parelles d'equips (sense importar qui és local)
    # Per evitar duplicats (ex: Real Madrid-Barcelona i Barcelona-Real Madrid), ordenem els noms alfabèticament
    edges_counts = {}
    for _, row in filtered_df.iterrows():
        team_a, team_b = sorted([row["HomeTeam"], row["AwayTeam"]])
        pair = (team_a, team_b)
        edges_counts[pair] = edges_counts.get(pair, 0) + 1

    # 3. Inicialitzar el graf no dirigit de NetworkX
    graph_obj = nx.Graph()

    # Afegir les connexions (edges) amb el seu pes (nombre de partits)
    for (u, v), weight in edges_counts.items():
        graph_obj.add_edge(u, v, weight=weight)

    # 4. Configurar la disposició i el disseny visual del graf
    plt.figure(figsize=(8, 8))
    
    # Utilitzem una disposició circular per veure clarament el pentàgon d'equips
    pos = nx.circular_layout(graph_obj)

    # Dibuixar els nodes (equips)
    nx.draw_networkx_nodes(
        graph_obj, pos, node_color="amber" if "amber" in locals() else "#FFD700",
        node_size=2500, edgecolors="black"
    )

    # Dibuixar les etiquetes amb els noms dels equips
    nx.draw_networkx_labels(graph_obj, pos, font_size=10, font_weight="bold", font_family="sans-serif")

    # Dibuixar les línies de connexió (arestes)
    nx.draw_networkx_edges(graph_obj, pos, width=2, edge_color="gray", alpha=0.8)

    # Extraure i dibuixar els pesos (número de connexions) al costat de cada línia
    edge_labels = nx.get_edge_attributes(graph_obj, "weight")
    nx.draw_networkx_edge_labels(graph_obj, pos, edge_labels=edge_labels, font_size=11, font_weight="bold")

    # Finalitzar l'estètica
    plt.title("Graf d'Enfrontaments Directes entre el Top 5 Històric (1995-2025)", fontsize=14, weight="bold")
    plt.axis("off")
    plt.tight_layout()
    plt.show()