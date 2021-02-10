class Rectangle:
  def __init__(self, width, height):
    self.w = width
    self.h = height
  
  def __repr__(self):
    return f"Rectangle(width={self.w}, height={self.h})"

  def set_width(self, width):
    self.w = width
  
  def set_height(self, height):
    self.h = height
  
  def get_area(self):
    return self.w * self.h
  
  def get_perimeter(self):
    return 2*self.w + 2*self.h

  def get_diagonal(self):
    return (self.w ** 2 + self.h ** 2) ** .5

  def get_picture(self):
    return ("*"*self.w+"\n")*self.h if self.w<=50 and self.h<=50 else "Too big for picture."

  def get_amount_inside(self, temp):
    return (self.w // temp.w) * (self.h//temp.h)

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
    self.s = side
    self.set_width = self.set_height = self.set_side

  def __repr__(self):
    return f"Square(side={self.s})"

  def set_side(self,side):
    self.s = self.w = self.h = side
