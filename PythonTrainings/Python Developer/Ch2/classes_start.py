#
# Example file for working with classes
#



class rectangle():
  side1=1
  side2=1
  

  def __init__(self,side1,side2):
    self.side1=side1
    self.side2=side2

  def area(self):
    return self.side1 * self.side2

  def perimeter(self):
    return self.side1*2+self.side2*2

  def print(self):
    print("Area " , self.area(),"\n", "perimeter " , self.perimeter())
  
class square(rectangle):
 
  def __init__(self,side):
    self.side1=self.side2=side
 

def main():
  rect = rectangle(1,1)
  rect.print()

  squ = square(3)
  squ.print()


if __name__ == "__main__":
  main()
