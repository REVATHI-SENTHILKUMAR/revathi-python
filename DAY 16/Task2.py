file_name = "studentinfo.txt"

with open(file_name, "w") as file:
    file.write("Roll No: 01, Name: Revathi\n")
    file.write("Roll No: 02, Name: Geetha\n")
    file.write("Roll No: 03, Name: Senthil\n")

print(f"--- Data successfully written to {file_name} ---")

print("\nStudent Records from File:")
print("-" * 25)

with open(file_name, "r") as file:
    content = file.read()
    print(content)
