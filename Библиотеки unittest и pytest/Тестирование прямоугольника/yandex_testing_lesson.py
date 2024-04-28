class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        try:
            self.width = float(self.width)
            self.height = float(self.height)
        except Exception:
            raise TypeError

        if self.width < 0 or self.height < 0:
            raise ValueError

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2
