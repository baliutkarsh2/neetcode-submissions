class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        dq = deque()
        dq.append((0, -1))
        visited = set()
        visited.add(0)

        while dq:
            cur, parent = dq.popleft()
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