class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        count = 0

        for start in range(n):
            if start in seen:
                continue
            
            dq = deque()
            dq.append((start, -1))
            while dq:
                cur, parent = dq.pop()
                seen.add(cur)
                for nei in adj[cur]:
                    if nei == parent or nei in seen:
                        continue
                    dq.append((nei, cur))
                    seen.add(nei)
            count += 1
        return count


            