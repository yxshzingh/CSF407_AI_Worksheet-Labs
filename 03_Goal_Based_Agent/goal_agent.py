from collections import deque

GRID=[
'#####################',
'#S....#............G#',
'#.##....##########..#',
'#....##.............#',
'#.######.###.#.###..#',
'#........#..........#',
'#####################']
DIRS=[(-1,0),(1,0),(0,-1),(0,1)]

def find(grid,ch):
    for r,row in enumerate(grid):
        for c,v in enumerate(row):
            if v==ch:return(r,c)

def pathfind(grid):
    s,g=find(grid,'S'),find(grid,'G'); q=deque([s]); parent={s:None}
    while q:
        p=q.popleft()
        if p==g: break
        for dr,dc in DIRS:
            n=(p[0]+dr,p[1]+dc)
            if 0<=n[0]<len(grid) and 0<=n[1]<len(grid[0]) and grid[n[0]][n[1]]!='#' and n not in parent:
                parent[n]=p;q.append(n)
    if g not in parent:return None
    path=[];p=g
    while p is not None:path.append(p);p=parent[p]
    return path[::-1]

def main():
    p=pathfind(GRID)
    print('Algorithm: BFS goal-based path planning')
    print('Path found:',bool(p))
    print('Path length:',len(p)-1 if p else None)
    print('Path:',p)

if __name__=='__main__':main()
