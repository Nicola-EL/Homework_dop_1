grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
sort_ = sorted(students)
print(sort_)
# находим среднюю арифметическую по каждому ученику
s_a = sum(grades[0])/len(grades[0])
s_b = sum(grades[1])/len(grades[1])
s_j = sum(grades[2])/len(grades[2])
s_k = sum(grades[3])/len(grades[3])
s_s = sum(grades[4])/len(grades[4])
new_journal= [s_a, s_b, s_j, s_k, s_s]
finish_journal= (dict(zip(sort_,new_journal)))
print(finish_journal)














