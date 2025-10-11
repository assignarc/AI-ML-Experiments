#
# Example file for working with date information
#
from datetime import date, datetime, time, timedelta

class myDT():
  today=datetime.now()
  aprilfoolsday = date(today.year,4,1)
  
  def __init__(self,todayD):
    today=todayD

  def print(self):
    print(self.today)
    print(self.today.now().time())

  def increment(self, d):
    print(self.today+timedelta(days=d))
  
  def daystoAFD(self):
    todaydate = self.today.date()
    if date.today() > self.aprilfoolsday:
      print((date.today()-self.aprilfoolsday).day)
    else:
      print(self.aprilfoolsday-date.today().day)


def main():

  m = myDT(datetime.today)
  m.print()
  m.increment(12)
  m.daystoAFD()

  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class


  # print out the date's individual components

  
  # retrieve today's weekday (0=Monday, 6=Sunday)

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class


  # Get the current time


  
if __name__ == "__main__":
  main()
  