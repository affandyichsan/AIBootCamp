# manipulation data in a dictionary

person = {"name":"affandy", "age":20, "city":"Semarang", "grade":98}

person["addreess"] = "kanaya land6"
person["age"] = 32


if "grade" in person:
    del person["grade"]
    
    
print(person)