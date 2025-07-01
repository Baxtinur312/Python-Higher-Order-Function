prices = ["$120", "$340", "$50", "$90"]
filtered_prices  = filter(lambda price: price.startswith("$"), prices)
filtered_prices = map(lambda price: price[1:], filtered_prices)
filtered_prices = map(int, filtered_prices)
print(list(filtered_prices))