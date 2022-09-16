# Write your code here
global count
count = 0

def merge(A, B):
  
  (m, n) = (len(A), len(B))
  (C, i, j, k) = ([], 0, 0, 0)
  
  while (k < m+n):
    if i == m:
      C.extend(B[j:])
      k = k + (n-j)
    elif j == n:
      C.extend(A[i:])
      k = k + (m-i)
    elif A[i] < B[j]:
      C.append(A[i])
      (i, k) = (i+1, k+1)
    else:
      C.append(B[j])
      (j, k) = (j+1, k+1)
  return C

def mergesort(A):
  n = len(A)
  global count
  count += 1

  if len(A) == 2:
    count -= 2
  
  if n <= 1:
    return A
  
  L = mergesort(A[:n//2])
  R = mergesort(A[n//2:])

  B = merge(L, R)

  return (B)

def subordinates(A):
  global count
  L = mergesort(A)
  return L, count

# Suffix Code

print(subordinates(eval(input())))
