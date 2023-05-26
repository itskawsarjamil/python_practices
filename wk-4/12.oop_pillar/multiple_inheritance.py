class School:
    def __init__(self, name):
        self.school_name = name
        print('school init called')


class Grade:
    def __init__(self, grade_name):
        self.grade_name = grade_name
        print('grade class init called')

class SportsTeam:
    def __init__(self,sport_name):
        print('sportsteam called')
        self.sport_name=sport_name
        self.sport_player=[]
        
    def add_player(self,player_name):
        self.team.append(player_name)
        

class Student(School, Grade,SportsTeam):
    def __init__(self, name, grade_name, school_name,sport_name):
        self.name = name
        print("Student init called")
        Grade.__init__(self, grade_name)
        School.__init__(self, school_name)
        SportsTeam.__init__(self,sport_name)


ananta_j = Student('AJ', 'MBA', "UK School",'cricket')

print(ananta_j.name)
print(ananta_j.grade_name)
print(ananta_j.school_name)
ananta_j.sport_player.append('abc')
ananta_j.sport_player.append('def')
print(ananta_j.sport_player)