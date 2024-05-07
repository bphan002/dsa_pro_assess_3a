from collections import deque

class Solution:
    def minKnightMoves(self, x, y):
        #do not have to worry about out of bounds
        #bfs
        # 8 directions
        #needs to reach [x,y]
        visited = set()
        #row, col, distance
        queue = deque([(0,0,0)])

        DIRS = [[1,-2], [2,-1], [2, 1], [1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]

        while len(queue):
            row, col, distance = queue.popleft()
            
            if row == x and col == y:
                return distance
            
            for dir in DIRS:
                dr, dc = dir
                new_row = row + dr
                new_col = col + dc

                if (new_row,new_col) not in visited:
                    queue.append((new_row, new_col, distance +1))


