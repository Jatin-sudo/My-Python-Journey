PH_LEVELS = int(input("Enter ph value of your solution between 1-14 "))

if PH_LEVELS > 14:
  print("PH LEVELS CAN NOT BE THAT HIGH , IT SHOULD BE BETWEEN 1 - 14 ")
elif PH_LEVELS > 7:
  print ("Nature of your solution is Basic")
elif PH_LEVELS < 7:
  print ("Nature of your solution is Acidic")
else:
  print("Nature of your solution is Neutral")