Student_Gradebook={
    "Brogan":100,
    "Mya":87,
    'easton':80,
    'sarah':92,
    'john':89
    }
total_score=0
for student in Student_Gradebook:
    total_score+=Student_Gradebook[student]
avg=total_score/len(Student_Gradebook)
print(avg)
highest=max(Student_Gradebook,key=Student_Gradebook.get)
print(highest)
lowest=min(Student_Gradebook,key=Student_Gradebook.get)
print(lowest)
studentfinder=input('who are you looking for')
Student_Gradebook=Student_Gradebook.get(studentfinder,"notfound")
if Student_Gradebook!="notfound":
    print(f"{studentfinder}grade is {Student_Gradebook}")
else:
    print('sorry not found')

