def expanding(l):
  if len(l) <= 2:
    return (True)
    
  diff = abs(l[1]-l[0])
  
  for i in range(1,len(l)-1):
    diff2 = abs(l[i]-l[i+1])
    if diff2 <= diff:
      return False
    diff = diff2
    
  return True

# suffix code
L = eval(input())
print(expanding(L))
