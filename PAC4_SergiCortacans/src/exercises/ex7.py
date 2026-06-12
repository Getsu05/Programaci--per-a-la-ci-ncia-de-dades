"Exercici 7: Graf de connexions de xarxa."

import matplotlib.pyplot as plt
import networkx as nx


def graf(data, selected_teams):
    "Genera i dibuixa un graf de connexions entre els equips seleccionats."
    filtered_df = data[
        data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)
    ].copy()

    edges_counts = {}
    for _, row in filtered_df.iterrows():
        team_a, team_b = sorted([row["HomeTeam"], row["AwayTeam"]])
        pair = (team_a, team_b)
        edges_counts[pair] = edges_counts.get(pair, 0) + 1

    graph_obj = nx.Graph()
    for (u, v), weight in edges_counts.items():
        graph_obj.add_edge(u, v, weight=weight)

    plt.figure(figsize=(8, 8))
    pos = nx.circular_layout(graph_obj)

    nx.draw_networkx_nodes(graph_obj, pos, node_color="#FFD700", node_size=2500, edgecolors="black")
    nx.draw_networkx_labels(graph_obj, pos, font_size=10, font_weight="bold")
    nx.draw_networkx_edges(graph_obj, pos, width=2, edge_color="gray", alpha=0.8)

    edge_labels = nx.get_edge_attributes(graph_obj, "weight")
    nx.draw_networkx_edge_labels(graph_obj, pos, edge_labels=edge_labels, font_size=11, font_weight="bold")

    plt.title("Graf d'Enfrontaments Directes entre el Top 5 Històric (1995-2025)", fontsize=14, weight="bold")
    plt.axis("off")
    plt.tight_layout()