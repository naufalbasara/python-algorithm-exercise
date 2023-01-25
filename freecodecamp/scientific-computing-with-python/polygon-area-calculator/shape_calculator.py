class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width+self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return  "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
                if j == self.width-1:
                    picture += '\n'
        return picture
    
    def get_amount_inside(self, object):
        if self.get_area() < object.get_area():
            return 0
        elif self.get_area() == object.get_area():
            return 1
        return int(self.get_area()/object.get_area())

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height
        
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def get_area(self):
        return self.width**2

    def get_perimeter(self):
        return 4*(self.width)