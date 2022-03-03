import random

def count_sort(li,max_count):
    count=[0 for _ in range(max_count+1)]
    for val in li:
        count[val]+=1
    li.clear()
    for idx,val in enumerate(count):
        for i in range(val):
            li.append(idx)

li=[random.randint(0,10) for _ in range(20)]
print(li)
count_sort(li,10)
print(li)

