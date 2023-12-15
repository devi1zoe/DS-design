import networkx as nx
import matplotlib.pyplot as plt

class TopologicalSortGraph:
    def __init__(self, G):
        self.G = G

    def plot_topological_sort(self):
        plt.figure(figsize=(10, 8), dpi=300)

        # 计算拓扑排序
        topological_order = list(nx.topological_sort(self.G))

        # 将节点分层
        layers = {}
        for node in topological_order:
            in_edges = set(self.G.in_edges(node))
            if not in_edges:
                # 根节点，放在第一层
                layers[node] = 0
            else:
                # 将节点放在比其父节点层级加1的层
                parent_layer = max(layers[parent] for (parent, _) in in_edges)
                layers[node] = parent_layer + 1

        # 绘制图形
        max_layer = max(layers.values())
        pos = {node: (layers[node], -layers[node] / (max_layer + 1)) for node in topological_order}
        ppos = {node: (layers[node], -layers[node] / (max_layer + 1)) for node in topological_order}

        # 调整x坐标，确保同一层的节点有一定的间隔
        for layer in range(max_layer + 1):
            layer_nodes = [node for node in pos if layers[node] == layer]
            layer_width = len(layer_nodes)
            for i, node in enumerate(layer_nodes):
                pos[node] = (layers[node], -i / (0.01 * layer_width))
                ppos[node] = (layers[node], -i / (0.01 * layer_width) - 3)

        # 显示节点编号
        labels = {node: str(i + 1) for i, node in enumerate(topological_order)}
        nx.draw_networkx_labels(self.G, pos=pos, labels=labels, font_color="#FFFFFF", font_size=8)

        nx.draw_networkx_labels(self.G, pos=ppos, font_color="#B991F5",font_size=8)

        nx.draw(self.G, pos, node_color='#6272a4', edge_color='#BB8DFF', with_labels=False, arrows=True, connectionstyle='arc3,rad=0.01')

        # plt.savefig("b_data/final_data/信安专业课程拓扑.png", bbox_inches='tight', transparent=True)
        plt.savefig("b_data/final_data/计科专业课程拓扑.png", bbox_inches='tight', transparent=True)

        plt.show()