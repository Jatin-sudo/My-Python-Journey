Height = int(input("Enter your Height in cms : "))
Credits = int(input("How much credits do you have ? "))

if Height >= 137 and Credits >= 10:
  print ("Enjoy the Ride! ")
elif Height < 137 and Credits >= 10:
  print ("You are not tall enough to enjoy ride.")
elif Height >= 137 and Credits < 10:
  print ("You don't have enough credits to enjoy the ride.")
else:
  print ("You have not met any requirements to enjoy the ride")
