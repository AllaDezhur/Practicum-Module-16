from RECT import Rectangle_test, Square, Circle
rec_1 = Rectangle_test(3,4)
rec_2 = Rectangle_test(12,5)

print('Площадь прямоугольника 1 = ',rec_1.getArea())
print('Площадь прямоугольника 2 = ',rec_2.getArea())

sq_1 = Square(5)
sq_2 = Square(10)

print('Площадь квадрата 1 = ',sq_1.get_Area())
print('Площадь квадрата 2 = ',sq_2.get_Area())

circle_1 = Circle(5)
сircle_2 = Circle(10)

print('Площадь круга 1 = %.2f'% circle_1.get_area_cirle())
print('Площадь круга 2 = %.2f'% сircle_2.get_area_cirle())

figures = [rec_1,rec_2,sq_1,sq_2,circle_1,сircle_2]
for figure in figures:
    if isinstance(figure,Square):
        print(figure.get_Area())
    elif isinstance(figure,Circle):
        print(figure.get_area_cirle())
    else:
        print(figure.getArea())
