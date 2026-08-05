employees={
    "John":45000,
    "Emma":60000,
    "Michael":75000,
    "Sophia":52000,
    "James":48000
}

for name in employees:
    if employees[name]>50000:
        print(name,employees[name])

highest=max(employees,key=employees.get)
print(highest,employees[highest])