#for times in [5,2,5,2,2]:   
#    print("x" * times)
#this is the easy way, it is for cheating, but if we want to solve it with nested loop, here is the solution

for x_count in [5,2,5,2,2]:
    output = ""
    for times in range(x_count):
        output += "x"
    print(output) 

print(" ")

for x_count in [1,1,1,1,5]:
    output = ""
    for times in range(x_count):
        output += "x"
    print(output)   
