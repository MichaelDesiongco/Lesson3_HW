# 1 Python list transformation

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
          
grades_descending = sorted(grades, reverse=True)
print(f"Sorted grades: {grades_descending}")

average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade}")

# 2 Advanced List Methods and Identity Operators

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and attended:
    print("Alice has submitted their assignment and attended class")
else: 
    print("Alice is not in the list")

# 3 Advanced Slicing Techniques

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 
                92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print(f"Second week temperatures: {second_week_temperatures}")

temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print(f"Temperatures above 100: {temperatures_above_100}")