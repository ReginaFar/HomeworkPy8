# Задание 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
#  конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования
#  матрицы.[[], [], []]
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
# в привычном виде.

# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix
        

    def __str__(self):
        return '\n'.join('\t'.join(map(str, my_matrix)) for my_matrix in self.my_matrix)


    def __add__(self,other):
        result = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.my_matrix)):
            for j in range(len(other.my_matrix[i])):
                result[i][j] = self.my_matrix[i][j] + other.my_matrix[i][j]
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1 + matrix_2)
