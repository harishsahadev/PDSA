#Write your code here
def findPair(L, pairsum):
  L.sort()
  if pairsum < L[0]+L[1]:
    return False
  if len(L) <= 1:
    return False
  for i in range(len(L)-1):
    for j in range(i+1, len(L)):
      if pairsum == (L[i] + L[j]):
        return True
  return False


# Suffix code
L = [int(item) for item in input().split()]
pairsum = int(input())
print(findPair(L, pairsum))
