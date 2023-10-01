# Доработаем задания 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from task_6 import Dog
from task_6 import Cat
from task_6 import Bird
    

class Factory:
    def get_type(self, type_, name, age, spec):
        if type_=='dog':
            return Dog(name, age, spec)
        elif type_=='cat':
            return Cat(name, age, spec)
        elif type_=='bird':
            return Bird(name, age, spec)
        else:
            return ValueError    
    
    def type_f(self):
        self.type_=self
        
f=Factory()
dog=f.get_type('dog','Bob', 5, 'гавкает')
cat = f.get_type('cat',"Marusa", 2, "мурлыкает")
bird = f.get_type('bird',"Aro", 1, "поет")


# print(dog.__dict__)
# print(cat.__dict__)
# print(bird.__dict__)


print(f'имя: {dog.name}, возраст: {dog.age} лет, действия: {dog.spec}')
print(f'имя: {cat.name}, возраст: {cat.age} лет, действия: {cat.spec}')
print(f'имя: {bird.name}, возраст: {bird.age} лет, действия: {bird.spec}')

