#write your code here
class Queue:
  def __init__(self):
    self.queue = []
  
  def addq(self, v):
    self.queue.append(v)

  def delq(self):
    v = None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
    return v

  def isempty(self):
    return (self.queue == [])

  def __str__(self):
    return str(self.queue)

def BFSListPath(AList, v):
  visited, parent = {}, {}
  for i in AList.keys():
    visited[i] = False
    parent[i] = -1
  q = Queue()

  visited[v] = True
  q.addq(v)

  while(not q.isempty()):
    j = q.delq()
    for k in AList[j]:
      if (not visited[k]):
        visited[k] = True
        parent[k] = j
        q.addq(k)
  
  return parent

def findpath(AList, a, b):
  P = BFSListPath(AList, b)
  i = a
  path_list = []
  while (i in P.keys()):
    path_list.append(i)
    i = P[i]
  return path_list

def backandforth(AList, end2, end1):
  path_list = []
  path_list = findpath(AList, end1, end2)
  count = 0
  while(len(path_list) != 1):
    count += 1
    # print(path_list)
    path_list.remove(end1)
    path_list.remove(end2)
    # print(path_list)
    
    for i in path_list:
      for j in AList.keys():
        if i == j:
          del AList[j]
          break
      for j in AList.keys():
        for k in AList[j]:
          if k == i:
            AList[j].remove(i)
    path_list = findpath(AList, end1, end2)
  return count
    
    
#Suffix Code
end1 = int(input())
end2 = int(input())

AList = {}

while True:
    line = input()
    if line.strip() == '':
        break
    u, vs = line.strip().split(':')
    u = int(u)
    AList[u] = []
    for v in vs.strip().split():
        v = int(v)
        if v not in AList:
            AList[v] = []
        AList[u].append(v)

print(backandforth(AList, end1, end2))
