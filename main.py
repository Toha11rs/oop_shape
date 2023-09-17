from square import Circle, Triangle


shapes = [ Circle(3),Triangle(3,4,5)]

for shape in shapes:
    print(f"площадь {shape.name()} равна {round(shape.square(),2)}")