count = int(input("how many items in list? "))
list = []
remove_items_index_list = []

for k in range(count):
    p = int(input())
    list.append(p)
print(list)

list.sort()
list.reverse()

for i in range(count-1):
    if list[i+1] == list[i]:
        remove_items_index_list.append(i)

print(remove_items_index_list)
print(list)

for items in remove_items_index_list:
    list.pop(items)

print(list)
