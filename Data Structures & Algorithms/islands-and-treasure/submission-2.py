class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        dq = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dq.append((i, j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq:
            r, c = dq.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == INF:
                    grid[nr][nc] = grid[r][c] + 1
                    dq.append((nr, nc))


