
from email import emailAdress
from first import firstName
from id import idNum
from last import lastName

import random

def printInfo(user):
  print("ALERT: User", user, "has accessed the system!")
  print("The First Name is:", (random.choice(firstName)))
  print("The Last Name is:", (random.choice(lastName)))
  print("The ID # is:", (random.choice(idNum)))
  print("The Email Address is:", (random.choice(emailAdress)))
  print()

printInfo("Jose")
printInfo("Ernesto")
printInfo("Camilo")
printInfo("Galia")