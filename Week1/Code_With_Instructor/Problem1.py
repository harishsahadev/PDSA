import math
def prime(n):
  (result, i) = (True, 2)
  while (result and (i <= math.sqrt(n))):
    if (n%i) == 0:
      result = False
    i = i+1
  return result

def factors(n):
  factorlist = []
  for i in range(1, n+1):
    if n%i == 0:
      factorlist.append(i)
  return factorlist

def primeproduct(m):
  factorlist = factors(m)
  for i in range(len(factorlist)):
    for j in range(len(factorlist)):
      if ((factorlist[i]*factorlist[j]) == m) and prime(factorlist[i]) and prime(factorlist[j]):
        return True
  return False


#Suffix Code
n = int(input())
print(primeproduct(n))
