'''''''''''''''''
Write a python program to give a detailed report of 15 days python training which includes
1.day
2.Topics covered
3.Efficiency (Rate of Efficiency & grip on topics learnt on scale of 5 )
4.Number of Assignment Questions Sloved
5.NUmber of Hackerrank Questions Solved
6.Ratings Acheived on Hackerrank For the particular day
7.Certificates completed
8.Duration Of cls
9.Rate of session on scale of 5 where
i)1 - being worst
ii)2-being bad
'''''''''''''''''

class Review():
  def __init__(self,day,topics,efficiency,qsolved,hsolved,ratingonrank,certificates,duration,sessionrating):
    self.rday=day
    self.rtopics=topics
    self.refficiency=efficiency
    self.rqsolved=qsolved
    self.rhsolved=hsolved
    self.rratingonrank=ratingonrank
    self.rcertificates=certificates
    self.rduration=duration
    self.rsessionrating=sessionrating
def display(self):
  print("Review on Python Programming")
  print(f"Day is {self.rday}")
  print(f"topic is {self.rtopics}")
  print(f"efficiency is {self.refficiency}")
  print(f"qsolved is {self.rqsolved}")
  print(f"hsolved is {self.rhsolved}")
  print(f"ratingonrank is {self.rratingonrank}")
  print(f"certificates is {self.rcertificates}")
  print(f"duration is {self.rduration}")
  print(f"sessionrating is {self.rsessionrating}")
r1=Review("1","Basic","3","5","0","0","1","2hr","3")
r2=Review("2","operators","4","5","0","0","1","2hr","3")
r3=Review("3","variables","3","5","0","0","2","2hr","3")
r4=Review("4","Loops","3","5","0","0","1","2hr","3")
r5=Review("5","Statments","4","5","0","0","1","2hr","3")
display(r1)
print()
display(r2)
print()
display(r3)
print()
display(r4)
print()
display(r5)