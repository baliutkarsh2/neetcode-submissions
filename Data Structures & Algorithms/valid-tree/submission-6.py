class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        dq = deque()
        seen = set()
        dq.append((0, -1))
        while dq:
            cur, parent = dq.pop()
            seen.add(cur)
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                seen.add(nei)
                dq.append((nei, cur))
        
        return True if len(seen) == n else False