def shuffle(l1, l2):
  new_list = []
  a = min(len(l1), len(l2))
  #print(a)
  
  for i in range(a):
    new_list.append(l1[i])
    new_list.append(l2[i])

  #print(new_list)
  
  if len(l1) < len(l2):
    new_list += l2[a : len(l2)]
  elif len(l1) > len(l2):
    new_list += l1[a : len(l1)]

  return new_list
  
# suffix Code
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))
