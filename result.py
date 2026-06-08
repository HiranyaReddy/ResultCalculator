name = input("Enter Student Name: ")

m1 = int(input("Enter Subject 1 Marks: "))
m2 = int(input("Enter Subject 2 Marks: "))
m3 = int(input("Enter Subject 3 Marks: "))

total = m1 + m2 + m3
percentage = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
else:
    print("Grade: D")
