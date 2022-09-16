# Write your code here
def binarysearch(L, v):
  s = 0
  e = len(L) - 1
  m = 0
  while s <= e: 
    m = s + (e - s) // 2
    if L[m] < v:
      s = m + 1
    elif L[m] > v:
      e = m - 1
    else:
      return True
  return False
  
def findCommonElements(A, B):
  n = len(A)
  A.sort()
  B
  L = []
  for i in range(n):
    if binarysearch(A, B[i]):
      L.append(B[i])
  return L
    
# Suffix code
A = eval(input())
B = eval(input())
result = findCommonElements(A, B)
result.sort()
print(result)
