data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
filtered_data = []
for x in data:
    if type(x) == str and len(x) > 5:
        filtered_data.append(x)
print(filtered_data)  # Output: ['banana', 'elephant']