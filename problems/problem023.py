def shortest_path(maze: [[bool]], start: (int,int), end: (int,int)) -> int:
    """You are given an M by N matrix consisting of booleans that represents
    a board. Each True boolean represents a wall. Each False boolean
    represents a tile you can walk on. Given this matrix, a start coordinate,
    and an end coordinate, return the minimum number of steps required to
    reach the end coordinate from the start. If there is no possible path,
    then return null. You can move up, left, down, and right. You cannot move
    through walls. You cannot wrap around the edges of the board."""
    queue = [(start, 0)]
    while len(queue) != 0:
        ((x,y), moves) = queue.pop(0)
        # are we at the end?
        if end == (x,y):
            return moves
        for xx,yy in [(1,0), (0,1), (-1,0), (0,-1)]:
            # check for within bounds
            if xx+x >= len(maze) or xx+x < 0:
                continue
            if yy+y >= len(maze) or yy+y < 0:
                continue
            # find the next moves
            if maze[x+xx][y+yy] == False:
                queue.append(((x+xx,y+yy), moves+1))
    return None
