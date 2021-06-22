list = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
g1=[]
g2=[]
    
def quick(a):
    pivot = a[len(a)-1]
    while a[0] != pivot:
        if a[0] < pivot:
            g1.insert(0,list[0])
            a.pop(0)
            continue
        elif a[0] > pivot:
            g2.insert(0,list[0])
            a.pop(0)
            continue
   
    return a

quick(list)

print(list)
print(g1)
print(g2)
 
# print(list) - [5] -> 함수외부에 있는 list값에 함수 안의 .pop는 영향을 주는데 
#g1+a+g2 는 영향을 안주는 이유?


