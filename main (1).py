def isleapyear(year):
    if(year%4==0 and year%100!=0 or year%400==0):
      return true
    else:
         return false
print("enter a year")
year=int(input ())
if isleapyear(year):
   print(yea)
      