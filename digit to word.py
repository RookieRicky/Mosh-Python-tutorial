phone = input(f" Place your phone number!")

digit_dict = {
    "1" : "one",
    "2" : "two",
    "3" : "three", 
    "4" : "four"
}
put = ""
putput = ""
for ch in phone:
    putput += digit_dict.get(ch, "I'mma yelling at yaaaaa!!") + " "

print(putput)
