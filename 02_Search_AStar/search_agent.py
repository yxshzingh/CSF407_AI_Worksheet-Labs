import heapq
from collections import deque

WAREHOUSE = [
'#################',
'#S....#.........#',
'#.###.#.#######.#',
'#...#.#.......#.#',
'###.#.#######.#.#',
'#...#.........#.#',
'#.###########.#.#',
'#.............#G#',
'#################']

DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def locate(grid, ch):
    for r,row in enumerate(grid):
        for c,v in enumerate(row):
            if v == ch: return (r,c)
    raise ValueError(ch)

def neighbors(grid, p):
    r,c=p
    for dr,dc in DIRS:
        q=(r+dr,c+dc)
        if 0 <= q[0] < len(grid) and 0 <= q[1] < len(grid[0]) and grid[q[0]][q[1]] != '#':
            yield q

def manhattan(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
def euclidean(a,b): return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

def astar(grid, heuristic=manhattan):
    start,goal=locate(grid,'S'),locate(grid,'G')
    heap=[(heuristic(start,goal),0,start)]
    g={start:0}; parent={start:None}; expanded=0; closed=set()
    while heap:
        f,curg,cur=heapq.heappop(heap)
        if cur in closed: continue
        closed.add(cur); expanded += 1
        if cur==goal:
            path=[]
            while cur is not None: path.append(cur); cur=parent[cur]
            return path[::-1],expanded
        for nxt in neighbors(grid,cur):
            ng=curg+1
            if ng < g.get(nxt,10**9):
                g[nxt]=ng; parent[nxt]=cur
                heapq.heappush(heap,(ng+heuristic(nxt,goal),ng,nxt))
    return None,expanded

def bfs(grid):
    start,goal=locate(grid,'S'),locate(grid,'G')
    q=deque([start]); parent={start:None}; expanded=0
    while q:
        cur=q.popleft(); expanded += 1
        if cur==goal:
            path=[]
            while cur is not None: path.append(cur); cur=parent[cur]
            return path[::-1],expanded
        for nxt in neighbors(grid,cur):
            if nxt not in parent:
                parent[nxt]=cur; q.append(nxt)
    return None,expanded

def run_tests():
    p,e=astar(WAREHOUSE)
    assert p and p[0]==locate(WAREHOUSE,'S') and p[-1]==locate(WAREHOUSE,'G')
    print('Original A*: found=',bool(p),'length=',len(p)-1,'expanded=',e)
    pb,eb=bfs(WAREHOUSE)
    print('Original BFS: found=',bool(pb),'length=',len(pb)-1,'expanded=',eb)
    assert len(pb)==len(p)
    trivial=['#####','#SG.#','#####']
    p2,e2=astar(trivial); assert len(p2)-1==1
    print('Trivial A*: length=',len(p2)-1,'expanded=',e2)
    no=['#######','#S....#','###.###','#...#G#','#######']
    p3,e3=astar(no); assert p3 is None
    print('No-solution A*: found=',bool(p3),'expanded=',e3)
    alt=['#######','#S...G#','#.#.#.#','#.....#','#######']
    p4,e4=astar(alt); assert p4 and len(p4)-1==4
    print('Alternative paths A*: length=',len(p4)-1,'expanded=',e4)
    for name,h in [('Manhattan',manhattan),('Zero',lambda a,b:0),('Euclidean',euclidean),('2x Manhattan',lambda a,b:2*manhattan(a,b))]:
        pp,ee=astar(WAREHOUSE,h); print(name, 'found=',bool(pp), 'length=',len(pp)-1 if pp else None,'expanded=',ee)

if __name__=='__main__': run_tests()
