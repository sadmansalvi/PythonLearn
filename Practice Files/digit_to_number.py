phone = input("Phone: ")

#introducing a dictionary
digits_mapping = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four"
}

phonetic = ""
for ch in phone:
    phonetic += (digits_mapping.get(ch, "Fool")) + " "

print(phonetic)

