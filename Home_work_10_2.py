# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c — стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def check_triangle(self):
        if self.a>(self.b+self.c) or self.b>(self.a+self.c) or self.c>(self.a+self.b):
            return 'Такого треугольника не существует'
        elif self.a==self.b==self.c:
            return 'Треугольник равносторонний'
        elif self.a==self.b or self.a==self.c or self.b==self.c:
            return 'Треугольник равнобедренный'
        else:
            return 'Треугольник разносторонний'



tri_1=Triangle(3,5,7)
tri_2=Triangle(1,5,7)
tri_3=Triangle(9,5,7)

print(tri_1.check_triangle())
print(tri_2.check_triangle())
print(tri_3.check_triangle())
