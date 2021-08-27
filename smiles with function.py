def emoji_convertor(message):
    words = message.split(" ")
    
    emoji_dict = {
        ":)": "😀",
        ":(": "😥", 
        "^-^": "😂"
    }
    
    output = ""
    for word in words:
        output += emoji_dict.get(word, word) + " Hi "
    return output


message = input("> ")
print(emoji_convertor(message))
