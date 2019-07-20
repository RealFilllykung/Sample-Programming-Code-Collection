from people import People
class salaryman:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    
    def jump(self):
        print(self.name + "is jumping with an occupation of " + self.occupation)

salaryman1 = salaryman("Fill",20,"Youtuber")
salaryman1.jump()