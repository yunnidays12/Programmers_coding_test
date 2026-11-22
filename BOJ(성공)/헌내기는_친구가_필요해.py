#헌내기는 친구가 필요해 (#21736)
def dfs(path, start, visited):
    visited[start] = True
    answer = 0

    x, y = coordinate[start]

    if map1[x][y] == "P":
        answer += 1

    for next in path[start]:
        if not visited[next]:
            answer += dfs(path, next, visited)

    return answer

n,m = map(int, input().split())
x, y = 0, 0

map1 = []
for i in range(n) :
  input_map = list(input())
  map1.append(input_map)

coordinate = []
for i in range(n) :
  for j in range(m) :
    if map1[i][j] == "0" or map1[i][j] == "P" :
      coordinate.append([i,j])
    elif map1[i][j] == "I" :
      start_x, start_y = i,j
      coordinate.append([i,j])

start = coordinate.index([start_x, start_y])
path = [[] for _ in range(len(coordinate))]
visited = [False for _ in range(len(path))]

dx, dy = [0,0,-1,1], [1,-1,0,0]
for i in range(len(coordinate)) :
  x, y = coordinate[i][0], coordinate[i][1]
  for j in range(0, 4) :
    nx,ny = x+dx[j], y+dy[j]
    if [nx, ny] in coordinate :
      b=coordinate.index([nx,ny])
      path[i].append(b)
      path[b].append(i)

answer = dfs(path, start, visited)
if answer == 0 : print("TT")
else : print(answer)
