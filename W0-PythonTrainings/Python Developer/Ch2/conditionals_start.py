#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 10

  if(x>y):
    print("X is greater")
  elif(x<y):
    print("X is less")
  else:
    print("they are equal")

  print("x is greater") if (x>y)  else print("Same") 

  # conditional flow uses if, elif, else  

  # conditional statements let you use "a if C else b"
  

if __name__ == "__main__":
  main()
