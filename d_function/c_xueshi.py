import networkx as nx

from d_function import a_topology
from PySide6.QtWidgets import QInputDialog

def xueshi_judge(all_xuefen, G, classandxueshidata_dict):
    gg, topo_subsets = a_topology.topo_sort(G)
    for original_subset in topo_subsets:
        for item in original_subset:
            if str(item) not in classandxueshidata_dict.keys() and "无意义" not in str(item):
                classandxueshidata_dict[str(item)] = 32  # 自动设置为32学时
    print("课程学时信息", classandxueshidata_dict)

    processed_subsets = []  # 用于存储处理后的子集
    for topo_subset in topo_subsets:
        for item in original_subset:
            if "无意义" in str(item):
                classandxueshidata_dict[str(item)] = 0
        one_subset_total_xuefen = sum(int(classandxueshidata_dict[str(classs)]) for classs in topo_subset)
        while one_subset_total_xuefen > all_xuefen:
            exceed_xuefen = one_subset_total_xuefen - all_xuefen
            print(f"警告：当前学期的课程子集总学时超过了指定的总学时 {all_xuefen}，超出 {exceed_xuefen} 学时.")
            min_xueshi_item = min(topo_subset, key=lambda class1: int(classandxueshidata_dict[str(class1)]))
            print(f"需要删除课程 '{min_xueshi_item}' 以调整总学时.学时：{classandxueshidata_dict[min_xueshi_item]}")

            node_to_adjust = str(min_xueshi_item)
            gg = a_topology.add_virtual_node(gg, node_to_adjust)
            one_subset_total_xuefen = one_subset_total_xuefen - int(classandxueshidata_dict[node_to_adjust])
            topo_subset.remove(node_to_adjust)
        processed_subsets.append(topo_subset)  # 记录处理后的子集
        gg, topo_subsets = a_topology.topo_sort(gg)
        # 更新总学时
        one_subset_total_xuefen = sum(int(classandxueshidata_dict[str(item)]) for item in topo_subset)
        print("第？学期的总学时：", one_subset_total_xuefen)
        print("这个学期的分学时：", end=" ")
        for item in topo_subset:
            print(classandxueshidata_dict[str(item)], end=" ")
        print("\n")

    print(processed_subsets)
    return processed_subsets
