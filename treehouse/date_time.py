import datetime

now = datetime.datetime.now()
two = now.replace(hour=20, minute = 5)
two.minute

print(two)

def minutes(timeA, timeB):
  time = round((timeB-timeA).seconds)
  print (time)

minutes(two, now)

file_object = open('game.txt')
data = file_object.read()
import re
re.search