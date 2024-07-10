grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Aaron_grades = sum(grades[0])/len(grades[0])
print(Aaron_grades)
Bilbo_grades = sum(grades[1])/len(grades[1])
print(Bilbo_grades)
Johnny_grades = sum(grades[2])/len(grades[2])
print(Johnny_grades)
Khendrik_grades = sum(grades[3])/len(grades[3])
print(Khendrik_grades)
Steve_grades = sum(grades[4])/len(grades[4])
print(Steve_grades)
students_grades = {'Aaron': Aaron_grades, 'Bilbo': Bilbo_grades, 'Johnny': Johnny_grades, 'Khendrik': Khendrik_grades, 'Steve': Steve_grades}
print(students_grades)