

students = {
    "Ali": 85,
    "Ahmed": 92,
    "Sara": 78
}

# Highest marks
highest = max(students.values())
print("Highest Marks:", highest)

# Average marks
total = sum(students.values())
count = len(students)

average = total / count
print("Average Marks:", average)