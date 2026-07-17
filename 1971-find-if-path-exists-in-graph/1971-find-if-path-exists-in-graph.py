class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)
