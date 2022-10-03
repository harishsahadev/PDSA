# Suffix Code
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

def minimumhops(AList, start, end):
  a = end
  b = start
  P = BFSListPath(AList, b)
  i = a
  path_list = []
  while (i in P.keys()):
    path_list.append(i)
    i = P[i]
  # print(path_list)
  return path_list




start = int(input())
end = int(input())
AList = eval(input())
shortestpath = minimumhops(AList, start, end)
print(len(shortestpath))
