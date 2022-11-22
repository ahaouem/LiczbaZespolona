# Write your class here
import math

class ComplexNumber:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        return ComplexNumber(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return ComplexNumber(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return ComplexNumber(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
        
    def __lt__(self, other):
        return math.sqrt(self.x2 + self.y**2) < math.sqrt(other.x**2 + other.y**2)

    def __gt__(self, other):
        return math.sqrt(self.x**2 + self.y**2) > math.sqrt(other.x**2 + other.y**2)

    def __eq__(self, other):
        return math.sqrt(self.x**2 + self.y**2) == math.sqrt(other.x**2 + other.y**2)

    def __str__(self):
        if self.y < 0:
            return str(self.x) + str(self.y) + 'i'
        elif self.y == 0:
            return str(self.x)
        elif self.x == 0:
            return str(self.y) + 'i'
        else:
            return str(self.x) + '+' + str(self.y) + 'i'

# Do not remove the following lines
if __name__ == '__main__':
  c1 = ComplexNumber(3,6)
  c2 = ComplexNumber(2,4)
  c3 = ComplexNumber(2,7)
  c4 = ComplexNumber(3,3)
  c5 = ComplexNumber(2,2)

  print(c1 + c2)
  print(c1 - c3)
  print(c1 * c2)
  print(c4 < c5)
