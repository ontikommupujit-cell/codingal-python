print("Star Pyramid")
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(i):
        print("* ", end="")
    print()
print("Floyd's Triangle")
rows = int(input("Enter the number of rows: "))
number = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()
print("Diamond Pattern")
rows = int(input("Enter the diamond row size: "))
if rows % 2 == 0:
    half_rows = rows // 2
else:
    half_rows = rows // 2 + 1
for i in range(1, half_rows + 1):
    for j in range(half_rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()

for i in range(half_rows - 1, 0, -1):
    for j in range(half_rows - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()