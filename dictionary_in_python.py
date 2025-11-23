#Dictionary

customer = {
    "name" : "John Smith",
    "age" : 30,    #each string should be uniquely named
    "is_verified" : True
}

print(customer["name"])

#or
print(customer.get("name"))

print(customer.get("nam")) #it does not cause error for nam when you use the get method unlike ["nam"]

#or you can supply a value to a non-existent attribute
print(customer.get("birthdate", "Jan 1, 1980"))

customer["name"] = "Jack Smith"
print(customer.get("name"))

#adding a new key
customer["Number of children"] = 2

print(customer.get("Number of children"))