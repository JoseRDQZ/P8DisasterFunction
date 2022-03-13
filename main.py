
from user import UserData
import random as rnd

users = UserData()
#users.printAllInfo()
#users.getUser("2271")
print(rnd.choice(list(users.allInfo.values())))