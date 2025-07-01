emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
filtered_emails = filter(lambda email: email.endswith("@gmail.com"), emails)
print(list(filtered_emails))