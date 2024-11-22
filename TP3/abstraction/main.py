from circle import Circle
from rectangle import Rectangle
from square import Square

# Test des classes
shapes = [Rectangle(3, 4), Square(5), Circle(2)]

for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print(f"  Aire = {shape.area():.2f}")
    print(f"  Périmètre = {shape.perimeter():.2f}")
