class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # If out of bounds or water, return 0
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            # Mark visited land as 0 (water)
            grid[r][c] = 0
            
            # Start area count
            area = 1
            
            # Explore 4 directions
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Calculate area for this island
                    island_area = dfs(r, c)
                    max_area = max(max_area, island_area)

        return max_area
