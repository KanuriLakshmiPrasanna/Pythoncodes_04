'''Find the least positive integer in a list'''
list_arr = [-1,1, 2, 3, 4, 5, 7, 8]
list_arr.sort()
lst = []

for i in range(1, max(list_arr) + 1):
    if i not in list_arr:
        lst.append(i)

if len(lst) == 0:
    print(max(list_arr) + 1)
else:
    print(lst[0])
