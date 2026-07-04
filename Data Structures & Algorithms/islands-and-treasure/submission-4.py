class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dq = deque()
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    dq.append((i, j))
        dist = 0
        while dq:
            for i in range(len(dq)):
                cur_i, cur_j = dq.popleft()
                seen.add((cur_i, cur_j))
                if grid[cur_i][cur_j] != 0 and dist < grid[cur_i][cur_j]:
                    grid[cur_i][cur_j] = dist
                for di, dj in dirs:
                    new_i, new_j = cur_i + di, cur_j + dj
                    if 0 <= new_i < rows and 0 <= new_j < cols and (new_i, new_j) not in seen and grid[new_i][new_j] == 0:
                        continue
                    if 0 <= new_i < rows and 0 <= new_j < cols and (new_i, new_j) not in seen and grid[new_i][new_j] == 2147483647:
                        dq.append((new_i, new_j))
                        seen.add((new_i, new_j))
            dist += 1
