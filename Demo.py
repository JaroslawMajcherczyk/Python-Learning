class Ractangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Szerokość musi być wieksza niż 0")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Wysokość musi być wieksza niż 0")

    @width.deleter
    def width(self):
        del self._width
        print("Szerokość została usunięta")
    @height.deleter
    def height(self):
        del self._height
        print("Wysokość została usunięta")



ractangle = Ractangle(3,4)

ractangle.width = 5
ractangle.height = 6

del ractangle.width
del ractangle.height


print(ractangle.width)
print(ractangle.height)