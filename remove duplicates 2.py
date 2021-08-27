numbers = [1,1,2,5,69,11,14,263,2,523,4,3,2,3,4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

numbers.sort()
uniques.sort()

print(numbers)
print(uniques)