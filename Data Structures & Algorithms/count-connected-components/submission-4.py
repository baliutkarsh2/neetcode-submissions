class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        count = 0
        visited = set()
        for start in range(n):
            if start in visited:
                continue
            # bfs(start)

            dq = deque()
            dq.append((start, -1))
            while dq:
                cur, parent = dq.popleft()
                visited.add(cur)
                for neighbor in adj[cur]:
                    if neighbor == parent:
                        continue
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dq.append((neighbor, cur))

            count += 1

        return count
        