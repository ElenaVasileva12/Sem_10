# Напишите функцию для транспонирования матрицы

import random

class Matrix:
    def __init__(self,row,column):
        self.row=row
        self.column=column

    def create_matrix(self):
        data = []
        for i in range(self.row):
            b = []
            for j in range(self.column):
                b.append(random.randint(0, 9))
            data.append(b)
        return data
    
    def output_matrix(self):
        a = self.create_matrix()
        for i in a:
            print(i)
        print()

        for j in range(self.column):
            for i in range(self.row):
                print(a[i][j], end=" ")
            print()       
    


mat_1=Matrix(5,4)
print(mat_1.output_matrix())

mat_2=Matrix(7,3)
print(mat_2.output_matrix())


