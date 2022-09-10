# write here
def del_char(s,c):
  str = ""
  if len(c) == 1:
    for ch in s:
      if ch != c:
        str = str + ch
  else:
    return s
  return str
    
        
# suffix code
s = input()
c = input()
print(del_char(s,c))
