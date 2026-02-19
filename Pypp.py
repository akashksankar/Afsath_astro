class_data = [
    {'name': 'Hari', 'place': 'TVM', 'mark': 60},
    {'name': 'Manu', 'place': 'Kollam', 'mark': 75},
    {'name': 'Ram', 'place': 'TVM', 'mark': 80}


for student in class_data:
    print(student['name'])

for student in class_data:
    if student['mark'] < 50:
        print(student)

]for student in class_data:
    if student['mark'] > 50:
        print(student)


for student in class_data:
    student['mark'] += 5
    if student['mark'] > 100:
        student['mark'] = 100

print(class_data)


for student in class_data:
    m = student['mark']
    
    if m >= 90:
        grade = 'A+'
    elif m >= 75:
        grade = 'A'
    elif m >= 60:
        grade = 'B'
    else:
        grade = 'C'
    
    student['grade'] = grade

print(class_data)
for student in class_data:
    student['department'] = {
        'dep_name': 'Computer Science',
        'hod_name': 'Dr. Nair'
    }

print(class_data)
