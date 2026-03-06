students = [
    {"name": "Arun", "marks": [78, 82, 90]},
    {"name": "Bala", "marks": [65, 70, 60]},
    {"name": "Chitra", "marks": [88, 92, 95]}
]

# 1. Calculate average for each student
averages = []
for s in students:
    avg = sum(s["marks"]) / len(s["marks"])
    averages.append({"name": s["name"], "avg": round(avg, 2)})

print(f"Averages: {averages}")


# 2. Find student with highest average
highest_student = max(averages, key=lambda x: x["avg"])
print(f"Highest Average: {highest_student['name']} ({highest_student['avg']})")



# 3. List students with average > 80
above_80 = [s["name"] for s in averages if s["avg"] > 80]
print(f"Students with > 80: {above_80}")
