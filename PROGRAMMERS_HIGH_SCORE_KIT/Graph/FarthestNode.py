def find_distance(edge_map):
    queue = [(1, 0)]
    visited = [0 for _ in range(len(edge_map))]
    length_from_one = [0 for _ in range(len(edge_map))]
    while queue:
        cur_node, cur_distance = queue.pop(0)
        if visited[cur_node] == 0:
            visited[cur_node] = 1
            length_from_one[cur_node] = cur_distance
            for connected_node in edge_map[cur_node]:
                queue.append((connected_node, cur_distance + 1))
    return length_from_one


def solution(n, edge):
    answer = 0

    edge_map = [[] for _ in range(n + 1)]

    for v0, v1 in edge:
        edge_map[v0].append(v1)
        edge_map[v1].append(v0)

    distances = find_distance(edge_map)
    farthest_distance = max(distances)
    for distance in distances:
        if distance == farthest_distance:
            answer += 1
    return answer
