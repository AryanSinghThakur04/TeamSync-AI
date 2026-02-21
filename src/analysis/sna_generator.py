import os
import networkx as nx
from pyvis.network import Network

def generate_sna(team_df):
    """
    Generates a SaaS-themed SNA graph.
    - Nodes: Indigo gradient (#1E3A8A to #3B82F6)
    - Background: Pure White
    - Edges: Soft Slate Grey
    """
    G = nx.Graph()
    names = team_df['Name'].tolist()
    
    for i, name1 in enumerate(names):
        for j, name2 in enumerate(names):
            if i < j:
                p1, p2 = team_df.iloc[i], team_df.iloc[j]
                synergy = (p1['Agreeableness'] + p2['Agreeableness']) / 2
                if synergy > 5:
                    G.add_edge(name1, name2, weight=synergy)

    centrality = nx.degree_centrality(G)
    max_cent = max(centrality.values()) if centrality else 0
    
    # SaaS Light Theme
    net = Network(height="450px", width="100%", bgcolor="white", font_color="#0F172A")
    
    for name in names:
        score = centrality.get(name, 0)
        size = 12 + (score * 20) 
        
        # Color palette shifted to Indigo/Blue
        is_central = (score == max_cent and max_cent > 0)
        color = "#1E3A8A" if is_central else "#3B82F6" 
        
        net.add_node(
            name, 
            label=name, 
            title=f"Centrality: {score:.2f}",
            size=size,
            color=color,
            borderWidth=2 if is_central else 1,
            shape="dot"
        )

    # Soft Slate Edges
    for u, v in G.edges():
        net.add_edge(u, v, color="#E2E8F0", width=2.5)

    net.toggle_physics(True)
    net.set_options("""
    {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -45,
          "centralGravity": 0.01,
          "springLength": 130,
          "springConstant": 0.08
        },
        "solver": "forceAtlas2Based"
      }
    }
    """)
    
    output_path = os.path.join(os.getcwd(), "team_network.html")
    net.write_html(output_path)