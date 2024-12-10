grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = list(students)
students_sort.sort()
students_ess = tuple(students_sort)

grades[0] = len(grades[0])/sum(grades[0])
grades[1] = len(grades[1])/sum(grades[1])
grades[2] = len(grades[2])/sum(grades[2])
grades[3] = len(grades[3])/sum(grades[3])
grades[4] = len(grades[4])/sum(grades[4])

students_sr_ball = {students_ess[0]: grades[0] , students_ess[1]: grades[1], students_ess[2]: grades[2], students_ess[3]: grades[3], students_ess[4]: grades[4]}
print(students_sr_ball)