import numpy as np

n = int(input('Amount of nodes: '))
m = int(input('Amount of edges: '))

def toMatrix(ribs):
  matrix = np.zeros((n, n), dtype=int)
  for i in ribs:
    matrix[i[0]][i[1]] = 1
    matrix[i[1]][i[0]] = 1
  print(matrix)

def toDict(n, m):
  ribs = list()
  for i in range(m):
    ribs.append(list(map(int, input('Edge: ').split())))

  toMatrix(ribs)

  ribsDict = dict()
  for i in range(n): # 0 1 2 3 4 5
    currRibs = []
    for j in range(m): # 0 1 2 3 4
      if ribs[j][0] == i:
        currRibs.append(ribs[j][1])
      elif ribs[j][1] == i:
        currRibs.append(ribs[j][0])
    ribsDict[i] = currRibs
  return ribsDict

ribsDict = toDict(n, m)
Visited = [False] * n

def DFS(start, verts):
  Visited[start] = True
  verts.append(start)
  for i in ribsDict[start]:
    if not Visited[i]:
      DFS(i, verts)
  return verts

comps = list()

for i in range(n):
  if not Visited[i]:
    comps.append(DFS(i, list()))

for i in range(len(comps)):
  print(*comps[i])
