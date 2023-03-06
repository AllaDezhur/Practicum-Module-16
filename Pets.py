class Pets:
    species = 'кот'
    def __init__(self, name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

cat1 = Pets("Сэм","мальчик",2)
cat2 = Pets("Барон", "мальчик", 2)
print (f' {cat1.__class__.species} -{cat1.name},{cat1.sex},{cat1.age}года')
print(f' {cat2.__class__.species} -{cat2.name},{cat2.sex},{cat2.age}года')


