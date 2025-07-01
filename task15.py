votes = [
  {"option": "A", "votes": 123},
  {"option": "B", "votes": 145},
  {"option": "C", "votes": 97}
]
most_voted_option = max(votes, key=lambda vote: vote["votes"])
print(f"Eng ko'p ovoz olgan variant: {most_voted_option['option']}, Ovozlar soni: {most_voted_option['votes']}")  # noqa: E501