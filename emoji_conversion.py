def emoji_converter(message):
    words = message.split(' ') #splits at spaces

    #dictionary of emojis
    emojis = {
        ":)" : "😁",
        ":(" : "🥲"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input(">")
result = emoji_converter(message)
print(result)