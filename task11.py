nums = list(range(1, 21))
even_nums = filter(lambda x: x % 2 == 0, nums)
squared_even_nums = map(lambda x: x ** 2, even_nums)   
print(list(squared_even_nums))