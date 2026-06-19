class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        dq = deque()
        dq.append((0, -1))
        visited = set()

        while dq:
            cur, parent = dq.pop()
            visited.add(cur)
            for neighbor in adj[cur]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                dq.append((neighbor, cur))
        
        if len(visited) != n:
            return False
        return True