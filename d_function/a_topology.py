import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['font.sans-serif'] = ['SimSun']
from PySide6 import QtWidgets
import copy
from PySide6.QtWidgets import QMessageBox
from c_Interface import page

def generate_Graph(filepath):
    df = pd.read_excel(filepath)
    G = nx.DiGraph()

    # 添加边到有向图，处理前置课程为 "无" 的情况
    for _, row in df.iterrows():
        if row[0] != "无":
            G.add_edge(row[0], row[1])
        else:
            G.add_edge(None, row[1])
    # 删除孤立的 None 节点
    G.remove_nodes_from([None])

    return G

def topo_sort(G):
    # 拓扑排序并划分子集
    subsets = []
    GG = copy.deepcopy(G)  # 使用深拷贝创建图对象的副本
    while G:
        current_subset = set()
        candidates = [node for node in G if len(list(G.predecessors(node))) == 0]
        # 如果没有明确先修课程的后修课程，将其放入第一个子集（S1）
        for node in candidates:
            current_subset.add(node)
            G.remove_node(node)
        for node in G.nodes:
            G.remove_edges_from([(node, n) for n in current_subset])
        subsets.append(current_subset)
    G = copy.deepcopy(GG)  # 使用深拷贝创建图对象的副本
    return G, subsets[:8]

virtual_node_count = 1
def add_virtual_node(G, adjust_class):
    if not G.has_node(adjust_class): G.add_node(adjust_class)

    global virtual_node_count
    # 添加虚拟节点和边
    virtual_node = f"无意义_{virtual_node_count}"
    virtual_node_count += 1
    page.data_dict[virtual_node] = 0

    G.add_node(virtual_node)
    for node in list(G.predecessors(adjust_class)):
        if G.has_node(node):
            if G.has_edge(node, adjust_class):
                G.add_edge(node, virtual_node)
                G.remove_edge(node, adjust_class)
        else:
            G.add_edge(node, virtual_node)

    G.add_edge(virtual_node, adjust_class)
    return G


def delete_virtual_node(self, G, adjust_class):
    predecessors_to_delete = list(G.predecessors(adjust_class))

    for node in predecessors_to_delete:
        if "无意义" in node:
            for prenode in list(G.predecessors(node)):
                G.add_edge(prenode, adjust_class)
                G.remove_edge(prenode, node)
            G.remove_edge(node, adjust_class)
            G.remove_node(node)
            break
        else:
            QMessageBox.warning(self, "警告", "该课程已是其可以在的学期的最前面！", QMessageBox.Ok)

    return G

def add_to_table(table, subsets):
    # 找到最长的集合的长度，即最大的 num_rows
    num_rows = max(len(subset) for subset in subsets)
    # 添加足够的行
    if table.rowCount() < num_rows:
        table.setRowCount(num_rows)

    for i, subset in enumerate(subsets, 1):
        # 如果subset一整个items都是"无意义"，则不进行处理
        if all("无意义" in str(item) for item in subset):
            i -= 1

        subset = [item for item in subset if "无意义" not in str(item)]
        for j, item in enumerate(subset, 0):
            table_item = QtWidgets.QTableWidgetItem(str(item))
            # 行j列i-1
            table.setItem(j, i - 1, table_item)
    return table


def find_node_and_successors(graph, start_node):
    if start_node not in graph.nodes:
        return None

    visited = set()
    result = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for successor in graph.successors(node):
                dfs(successor)

    dfs(start_node)
    return result



def find_node_and_predecessors(graph, start_node):
    if start_node not in graph.nodes:
        return None

    visited = set()
    result = []

    def dfs(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for predecessor in graph.predecessors(node):
                dfs(predecessor)

    dfs(start_node)
    return result
