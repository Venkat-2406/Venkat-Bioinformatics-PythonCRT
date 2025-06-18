'''''''''
you have participated the college-level coding fest which was there for 6 days

Write a python Program to give the final report which includes
1.Activities for the day including Timeline
2.Number of Teams/Participants for the day
3.Project_names
4.Technologies used
5.PPt demostration given
6.Winner of the day
7.Runner of the day
8.Best performer of day
9.Host of the program of that day
'''''''''''
class Report():
  def __init__(self,day,activites,teams,pname,technology,ppt,winner,runner,performer,Host):
    self.rday=day
    self.ractivites=activites
    self.rteams=teams
    self.rpname=pname
    self.rtechnology=technology
    self.rppt=ppt
    self.rwinner=winner
    self.rrunner=runner
    self.rperformer=performer
    self.rhost=Host
def display(self):
      print(f"Day: {self.rday}")
      print(f"Activities: {self.ractivites}")
      print(f"Participants: {self.rteams}")
      print(f"Project Names: {self.rpname}")
      print(f"Technologies Used: {self.rtechnology}")
      print(f"PPT Demonstrations Given: {self.rppt}")
      print(f"Winner of the Day: {self.rwinner}")
      print(f"Runner-up of the Day: {self.rrunner}")
      print(f"Best Performer of the Day: {self.rperformer}")
      print(f"Host of the Program for that Day: {self.rhost}")
      print("--------------------------------------------------")
# Creating 6 Report objects
R1 = Report("1", "Opening Ceremony, Team Introductions", 10, "Project A, Project B", "Python, JavaScript", "Yes", "Team Alpha", "Team Beta", "Alice", "John")
R2 = Report("2", "Workshops on Python and Web Development", 12, "Project C, Project D", "Python, HTML/CSS", "Yes", "Team Gamma", "Team Delta", "Bob", "Sarah")
R3 = Report("3", "Hackathon Begins, Team Collaboration", 15, "Project E, Project F", "Python, Flask", "Yes", "Team Epsilon", "Team Zeta", "Charlie", "Emma")
R4 = Report("4", "Midway Checkpoint, Team Presentations", 14, "Project G, Project H", "Python, Django", "Yes", "Team Eta", "Team Theta", "David", "Olivia")
R5 = Report("5", "Final Coding Sessions, Debugging", 13, "Project I, Project J", "Python, React", "Yes", "Team Iota", "Team Kappa", "Eve", "Liam")
R6 = Report("6", "Closing Ceremony, Awards Distribution", 16, "Project L, Project M", "Python, Node.js", "Yes", "Team Lambda", "Team Mu", "Frank", "Sophia")
# Displaying all reports
display(R1)
display(R2)
display(R3)
display(R4)
display(R5)
display(R6)
    
