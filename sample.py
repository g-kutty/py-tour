class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()
area = circle.area(25/2)
print(area)
