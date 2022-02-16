        
class Team(object):
    def __init__(self, name=None, logo=None, members=0):
        self.name = name
        self.logo = logo
        self.members = members

    def info(self):
        print(self.name,self.logo,self.members)


team = Team("Oscar", 0)

team2 = Team("Fred", members=0)


team3 = Team(name="Joe", members=0)
teamnumber=input("who are you, joe, Fred or Oscar, type 1 for Oscar, 2 for Fred, and 3 for Joe:")
action=input("if you want to view balance press 4, if you want to add to balance press 5, if you want to subtract from balance press 6")
if action == "4" and teamnumber == "1":
    print(team.members)
if action == "4" and teamnumber == "2":
    print(team2.members)
if action == "4" and teamnumber == "3":
    print(team3.members)
if action == "5" and teamnumber == "1":
    added=int(input("how much do you want to add put number value here"))
    team.members=team.members+added
    print(team.members)
if action == "5" and teamnumber == "2":
    added=int(input("how much do you want to add put number value here"))
    team2.members=team2.members+added
    print(team2.members)
if action == "5" and teamnumber == "3":
    added=int(input("how much do you want to add put number value here"))
    team3.members=team3.members+added
    print(team3.members)
if action == "6" and teamnumber == "1":
    subtracted=int(input("how much do you want to add put number value here"))
    team.members=team.members-subtracted
    print(team.members)
if action == "6" and teamnumber == "2":
    subtracted=int(input("how much do you want to add put number value here"))
    team2.members=team2.members-subtracted
    print(team2.members)
if action == "6" and teamnumber == "3":
    subtracted=int(input("how much do you want to add put number value here"))
    team3.members=team3.members-subtracted
    print(team3.members)