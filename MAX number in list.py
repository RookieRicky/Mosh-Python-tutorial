list_count = int(input("how many numbers are in the list? "))
list_of_number = []
for i in range(0, list_count):
    aka = int(input())

    list_of_number.append(aka) #is adding an element
print(list_of_number[:])

Max = list_of_number[0]

for n in range(1, list_count):
    if list_of_number[n] > Max:
        Max = list_of_number[n]
print(Max)        
