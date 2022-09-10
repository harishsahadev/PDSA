def histogram(l):
  d = {}
  for i in range(len(l)):
    if l[i] in d.keys():
      d[l[i]] += 1
    else:
      d[l[i]] = 1

  d_sorted_key = dict(sorted(d.items()))
  d_sorted_value = dict(sorted(d_sorted_key.items(), key=lambda item: item[1]))
  
  list = [(k, v) for k, v in d_sorted_value.items()]
  return list

# sufix code
L=eval(input())
print(histogram(L))
