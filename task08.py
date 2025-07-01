people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)