# write code here
def sumsquare(l):
  odd, even = 0, 0
  for i in range(len(l)):
    if l[i]%2 == 0:
      even += (l[i] * l[i])
    else:
      odd += (l[i] * l[i])
  return [odd, even]

# Suffix code
L = eval(input())
print(sumsquare(L))
