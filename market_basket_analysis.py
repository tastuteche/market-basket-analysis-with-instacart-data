import pandas as pd
import numpy as np
b_dir = '../instacart/order_products__prior.csv/'
b1_dir = '../instacart/products.csv/'

df = pd.read_csv(b_dir + 'order_products__prior.csv')
df_product = pd.read_csv(b1_dir + 'products.csv')
dic = df_product.set_index('product_id')['product_name'].to_dict()


def f(df, col1, col2):
    keys, values = df[[col1, col2]].sort_values(col1).values.T
    ukeys, index = np.unique(keys, True)
    arrays = np.split(values, index[1:])
    df2 = pd.DataFrame({col1: ukeys, col2: [list(a) for a in arrays]})
    return df2


# df_001 = df.sample(frac=0.0001)
# df_rest = df.loc[~df.index.isin(df_001.index)]

N = 1000
top_N = df['product_id'].value_counts()[:N].index
#[df_001['product_id'].isin(top_N)]
df_cart = f(df, 'order_id', 'product_id')
df_cart_multi = df_cart.loc[df_cart['product_id'].apply(len) > 4]
from mlxtend.preprocessing import OnehotTransactions
from mlxtend.frequent_patterns import apriori

oht = OnehotTransactions()
df_001 = df_cart_multi.sample(frac=0.001)
dataset = df_001['product_id'].tolist()
oht_ary = oht.fit(dataset).transform(dataset)
df_oht = pd.DataFrame(
    oht_ary, columns=[dic.get(id, id) for id in oht.columns_])
df_oht.mean(axis=0).describe()
frequent_itemsets = apriori(df_oht, min_support=0.005, use_colnames=True)
frequent_itemsets[frequent_itemsets['itemsets'].apply(len) > 1]

from mlxtend.frequent_patterns import association_rules

# association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.2)


import networkx as nx
G = nx.Graph()


for index, row in rules.iterrows():
    antecedants = ','.join(row['antecedants'])
    consequents = ','.join(row['consequents'])
    G.add_node(antecedants, node_size=row['antecedent support'])
    G.add_node(consequents, node_size=row['consequent support'])
    # G.add_weighted_edges_from(
    #    [(antecedants, consequents, row['lift'])])
    G.add_edge(antecedants, consequents,
               weight=row['lift'], edge_color=row['confidence'])

import seaborn as sns
colors = sns.mpl_palette("tab20", 20)

dic_node_size = nx.get_node_attributes(G, 'node_size')
dic_edge_weight = nx.get_edge_attributes(G, 'weight')
dic_edge_color = nx.get_edge_attributes(G, 'edge_color')
options = {
    'nodelist':  G.nodes(),
    'node_size': [dic_node_size[node] * 4000 for node in G.nodes()],
    'node_color': [colors[0] for n in G.nodes()],
    'edgelist': G.edges(),
    'width': [dic_edge_weight[edge] * 1.1 for edge in G.edges()],
    'edge_color': [dic_edge_color[edge] for edge in G.edges()],
    'with_labels': True,
    'alpha': 1,
    'font_weight': 'regular',
}

import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
pos = graphviz_layout(G, prog='neato', args="-Goverlap=scale")
# pos = nx.spring_layout(G, scale=3)
plt.figure(figsize=(15, 15))
nx.draw_networkx_nodes(G, pos, nodelist=options['nodelist'], node_size=options['node_size'],
                       node_color=options['node_color'], with_labels=True, alpha=0.7)
# alpha=0.2
# https://matplotlib.org/users/colormaps.html
draw_edges = nx.draw_networkx_edges(G, pos, edgelist=options['edgelist'],
                                    width=options['width'], edge_color=options['edge_color'], edge_cmap=plt.cm.hot, alpha=0.4)
nx.draw_networkx_labels(G, pos, font_size=9, font_color='r')
cbar = plt.colorbar(draw_edges)
cbar.ax.set_ylabel('# of confidence', rotation=290)
plt.axis('off')
import matplotlib.lines as mlines
blue_line = mlines.Line2D([], [], color=colors[0], marker='o',
                          markersize=15, label='graph node size:support')
import matplotlib.patches as mpatches
red_patch = mpatches.Patch(color='red', label='graph edge width:lift')
plt.legend(handles=[blue_line, red_patch])
# plt.show()
plt.savefig('mba.png', dpi=200)
plt.clf()
plt.cla()
plt.close()

from tabulate import tabulate
rules_print = rules.copy()
rules_print['consequents'] = rules_print['consequents'].apply(
    lambda x: ','.join(x))
rules_print['antecedants'] = rules_print['antecedants'].apply(
    lambda x: ','.join(x))
rules_print.drop(['antecedent support'], axis=1, inplace=True)
print(tabulate(rules_print, tablefmt="pipe", headers="keys"))
