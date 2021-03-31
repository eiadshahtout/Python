def build_person(first_name, last_name, age = None):
    person = {"first": first_name,
              "last" : last_name
			 }
    if age:
        person["age"] = 27
    return person
musician = build_person("Eiad","Shahtout", age = 27)
print(musician)