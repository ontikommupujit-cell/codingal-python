names=["Alex","Brian","Chris","David"]
roll_numbers=[101,102,103,104]
grades=["A","B+","A-","B"]

students=zip(names,roll_numbers,grades)

for name,roll,grade in students:
    print("Name:",name,"Roll Number:",roll,"Grade:",grade)