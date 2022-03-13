import json
class UserData:
    allInfo = {}
    def __init__(self):
        self.createAllInfo()
   
    def createAllInfo(self):
        self.allInfo = json.loads(open('data.json').read())

    def printAllInfo(self):
        print(json.dumps(self.allInfo, indent = 4, sort_keys=True))

    def addUser(self, firstName, lastName, idNum,  emailAddress):
        self.allInfo[idNum] = [{"firstName": firstName, "lastName" : lastName, "email" : emailAddress}]  
        json.dump(self.allInfo, open("data.json", 'w+'), ensure_ascii = True, indent = 4, sort_keys = True)
   
    def getUser(self, idNum: str):
        print(json.dumps(self.allInfo[str(idNum)], indent = 4, sort_keys = True))