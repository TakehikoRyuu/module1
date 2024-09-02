# Дополнительное практическое задание по модулю 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # Множество
StudSort = (sorted(students)) # отсортировал + перевёл в список для возможности доставать по индексу
Ratings = {StudSort[0] : (sum(grades[0])) / len(grades[0]),
           StudSort[1] : (sum(grades[1])) / len(grades[1]),
           StudSort[2] : (sum(grades[2])) / len(grades[2]),
           StudSort[3] : (sum(grades[3])) / len(grades[3]),
           StudSort[4] : (sum(grades[4])) / len(grades[4])}
print(Ratings) # {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}