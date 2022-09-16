# Write code here
def Findpeak(L):
  n = len(L)

  if n == 1:
    return L[1]
  if L[0] > L[1]:
    return L[0]
  if L[-1] > L[-2]:
    return L[-1]
  start = 0
  end = n-1
  while (start <= end):
    mid = start + (end - start) // 2
    if (L[mid] > L[mid-1]) and (L[mid] > L[mid+1]):
      return L[mid]
    else:
      if (L[mid-1] > L[mid] and L[mid+1] < L[mid]):
        end = mid
      else:
        start = mid

#Suffix Code
L = eval(input())
res = Findpeak(L)
print(res)
