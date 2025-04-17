
list1 = [1, 1, 2]
list2 = [2, 3, 4]
result=[x for x in list1 if x not in list2]+[x for x in list2 if x not in list1]
print(result)    