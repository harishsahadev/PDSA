# write you code here
def coolWorkers(AList, preference):
    (indegree,toposortlist) = ({},[])
    zerodegreeq = []

    for u in AList.keys():
        indegree[u] = 0
    
    for u in AList.keys():
        for v in AList[u]:
            indegree[v] = indegree[v] + 1
    
    for u in AList.keys():
        if indegree[u] == 0:
            zerodegreeq.append(u)
                
    while (len(zerodegreeq) > 0):
      for i in preference:
        if i in zerodegreeq:
          j = i
          zerodegreeq.remove(i)
          break
        # j = zerodegreeq.delq()
      toposortlist.append(j)
      indegree[j] = indegree[j]-1
      for k in AList[j]:
          indegree[k] = indegree[k] - 1
          if indegree[k] == 0:
              zerodegreeq.append(k)                
    return(toposortlist)




# Suffix Code
AList = eval(input())
preference = eval(input())
print(coolWorkers(AList, preference))
