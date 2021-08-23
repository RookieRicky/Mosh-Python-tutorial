weight = int(input("tell me your weight, plz "))
print(type(weight))
metrics = input("Type L for lbs and K for kilograms ")
if  metrics.lower == "l":
    Converted = float(weight) * 0.45
else:
    Converted = float(weight) / 0.45

# variables created in modules, fucntions, classes are recognized within them. But variables created in if or while statements are still recognized within the module, function or the class
# that includes the if or while statement
print(round(Converted, 2))
