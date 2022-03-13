import json
class UserData:
    def __init__(self, firstName, emailAddress, idNum, lastName):
        self.firstName = firstName 
        self.emailAddress = emailAddress 
        self.idNum = idNum 
        self.lastName = lastName
        self.allInfo = {}
   
    def createAllInfo(self):
        self.allInfo = json.loads(open('data.json').read())

    def printAllInfo(self):
        print(json.dumps(self.allInfo, indent = 4, sort_keys=True))