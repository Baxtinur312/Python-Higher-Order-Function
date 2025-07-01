text = ["apple", "34", "banana", "100", "abc", "75"]
sorted_numbers = sorted(
    filter(lambda x: x.isdigit(), text), 
)
sorted_numbers = list(map(int, sorted_numbers))
print(sorted_numbers)