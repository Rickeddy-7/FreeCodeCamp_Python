
class Rectangle:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def __str__(self):
        """returns an string instance of the object"""

        return f'Rectangle(width={self.width}, height={self.height})'

    def set_height(self,h):
        """changes the value of shape's height"""

        self.height = h
        return h
        
    def set_width(self,w):
        """changes the value of shape's width"""

        self.width = w
        return w

    def get_perimeter(self):
        """returns the perimeter of the shape"""
        
        perim = (self.height*2) + (self.width*2)
        return perim
    
    def get_area(self):
        """returns the area of the shape"""

        area = self.width * self.height
        return area

    def get_diagonal(self):

        diag = (self.width ** 2 + self.height ** 2) ** .5
        return diag

    def get_picture(self):
        """returns an ascii drawing of the shape"""

        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        else:
            picture = ''
            for i in range(self.height):
                for j in range(self.width):
                    picture += '*'
                picture += '\n'

            return picture

    def get_amount_inside(self,shape):
        """Returns the number of times the passed in shape could
           fit inside the shape(Rectangle) with no rotations."""

        if isinstance(shape,Rectangle) or isinstance(shape,Square):
            # first divide height of Rect(cls) by side lenght of shape
            num1 = self.height/shape.height
            # then divide the width of Rect(cls) by side lenght of shape
            num2 = self.width/shape.width
            # finally, return the product of num1 and num2
            return int(num1 * num2) 


class Square(Rectangle):

    def __init__(self,side_len):
        """returns width and height and also updates parent class"""

        super().__init__(side_len,side_len)
        self.side_lenght = side_len

    def __str__(self):
        return f'Square(side={self.side_lenght})'

    def set_side(self,n):
        """changes the side_length of the shape"""
        
        self.__init__(n)
        return n

    def set_width(self,n):
        self.set_side(n)

    def set_height(self,n):
        self.set_side(n)
