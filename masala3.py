class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def diameter(self):
        return self.radius * 2

doira = Circle(5)
print(doira.area())
print(doira.diameter())