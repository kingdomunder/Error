list = [11, 12, 6,8,3,9,10,1,2,4,7,5]
g1 = []
g2 = []

for x in range(0,int(len(list)/2)):
    g1.append(list[x])

for x in range (int(len(list)/2),len(list)):
    g2.append(list[x])

g1sorted = []
g2sorted = []

def Sort(group,sorted):
    sorted.insert(0, group[0])
    group.pop(0)
    indexNo = len(sorted)
    while len(group) != 0:
        if group[0] > sorted[indexNo-1]:
            sorted.insert(indexNo,group[0])
            group.pop(0)
            indexNo = len(sorted)
            continue
        elif indexNo == 1:
            sorted.insert(0,group[0])
            group.pop(0)
            indexNo = len(sorted)
            continue
        else:
            indexNo -= 1 

    return group , sorted

result = []

def MergeSort(g1sorted, g2sorted, result):
    while len(g1sorted) and len(g2sorted) != 0:
        if g1sorted[0] < g2sorted[0]:
            result.append(g1sorted[0])
            g1sorted.pop(0)
        elif g1sorted[0] > g2sorted[0]:
            result.append(g2sorted[0])
            g2sorted.pop(0)
    
    result = result + g1sorted
    result = result + g2sorted
    g1sorted.clear()
    g2sorted.clear()

    return g1sorted, g2sorted, result

Sort(g1,g1sorted)
Sort(g2,g2sorted)
print(MergeSort(g1sorted,g2sorted, result))






