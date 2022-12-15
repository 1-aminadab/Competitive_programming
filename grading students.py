
grade = [73, 67, 38, 33]
stu_grade = []


def differ(actual_grade, rounded_grade):
    if int(rounded_grade) - int(actual_grade) < 3:
        return int(rounded_grade)
    else:
        return int(actual_grade)
    

def gradingStudents(grades):

    for i in range(len(grades)):
        grade_pices = str(grades[i]).strip()
        last_pice = grade_pices[len(grade_pices) -1]
        if grades[i] < 38:
            stu_grade.append(grades[i])
        elif int(last_pice) <= 5:
            new_grade = "5".join(grade_pices)[0:2]
            stu_grade.append(new_grade)
            grades[i] = differ(grades[i], stu_grade[i])
        else:
            new_grade = "0".join(grade_pices)[0:2]
            stu_grade.append(int(new_grade ) + 10)
            grades[i] = differ(grades[i], stu_grade[i])
        print(grades[i])
gradingStudents(grade)
    
