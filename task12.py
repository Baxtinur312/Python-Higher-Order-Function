students = [
  {"name": "Aziz", "grade": 89},
  {"name": "Kamola", "grade": 95},
  {"name": "Javlon", "grade": 76}
]
highest_grade_student = max(students, key=lambda student: student["grade"])
print(f"Eng yuqori bahoga ega talaba: {highest_grade_student['name']})")