import pandas as pd
import networkx as nx
import re
import matplotlib.pyplot as plt

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel('snscrape1.xlsx')

# Extract the usernames from the tweet column using regular expressions
df['username'] = df['Tweet'].str.extract(r'@(\w+)')

# Create a list of unique usernames
users = list(df['username'].dropna().unique())

# Create an empty directed graph using NetworkX
G = nx.DiGraph()

# Add nodes to the graph for each user
for user in users:
    G.add_node(user)

# Add edges to the graph for each mention
for tweet in df['Tweet']:
    # Find all mentions in the tweet using regular expressions
    mentions = re.findall(r'@(\w+)', tweet)
    # Create edges between the mentioned users
    for i in range(len(mentions)):
        for j in range(i+1, len(mentions)):
            G.add_edge(mentions[i], mentions[j])

# Calculate the degree centrality of each node (user)
centrality = nx.degree_centrality(G)

# Sort the centrality dictionary by value in descending order
sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

# Get the top 10 most influential users
top_users = [user[0] for user in sorted_centrality[:10]]

# Create a subgraph of the top users
H = G.subgraph(top_users)

# Draw the graph using NetworkX and Matplotlib
pos = nx.spring_layout(H, k=0.5)
nx.draw(H, pos, with_labels=True, font_size=10, node_color='lightblue', edge_color='gray', width=1, alpha=0.7)
plt.show()
