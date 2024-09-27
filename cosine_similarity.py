# -*- coding:utf-8 -*-
import math
import json

def similarity_list(list1, list2):
    """
    Calculate the cosine similarity between two lists.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        float: The cosine similarity between the two lists. The value ranges from -1 (completely dissimilar)
               to 1 (identical), with 0 indicating orthogonality.
    """
    all_set = set(list1) | set(list2)
    list1_map = {}
    for s in list1:
        if s in list1_map:
            list1_map[s] += 1
        else:
            list1_map[s] = 1
    list2_map = {}
    for s in list2:
        if s in list2_map:
            list2_map[s] += 1
        else:
            list2_map[s] = 1
    list1_vec = []
    list2_vec = []
    for s in all_set:
        if s in list1_map:
            list1_vec.append(list1_map[s])
        else:
            list1_vec.append(0)

        if s in list2_map:
            list2_vec.append(list2_map[s])
        else:
            list2_vec.append(0)
    norm1 = math.sqrt(sum(list(map(lambda x: math.pow(x, 2), list1_vec))))
    norm2 = math.sqrt(sum(list(map(lambda x: math.pow(x, 2), list2_vec))))
    if norm1 * norm2 == 0:
        return 0
    cos = sum([list1_vec[i] * list2_vec[i] for i in range(0, len(list1_vec))]) / (norm1 * norm2)
    return cos

def similarity(data1, data2):
    """
    Calculate the similarity between two JSON objects.

    Args:
        data1 (dict): The first JSON object.
        data2 (dict): The second JSON object.

    Returns:
        float: A similarity score indicating how similar the internal order of the two JSON objects is.
    """
    return similarity_list(data1["_ord"], data2["_ord"])

if __name__ == '__main__':
    print(similarity_list(['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺', '备注'], ['材料牌号', '性能信息', '数据生产与审核', '标准', '加工工艺']))


