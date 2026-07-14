class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        v = [[False] * m for _ in range(n)]
        c = 0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not v[i][j]:
                    q.append((i,j))
                    c += 1
                while len(q) != 0:
                    s = q.popleft()
                    v[s[0]][s[1]] = True
                    for k in [(1,0), (-1,0), (0,1), (0,-1)]:
                        i1 = s[0] + k[0]
                        j1 = s[1] + k[1]
                        if i1 >= 0 and j1 >=0 and i1 < n and j1 < m:
                            if grid[i1][j1] == '1' and not v[i1][j1]:
                                q.append((i1, j1))
        return c
