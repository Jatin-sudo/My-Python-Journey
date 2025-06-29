import random

Question = input("Question : ")

Answer = random.randint (1 , 9)

if Answer == 1:
  print ("Magic 8 Ball :  Yes - definitely.")
elif Answer == 2:
  print ("Magic 8 Ball :  It is decidedly so.")
elif Answer == 3:
  print ("Magic 8 Ball :  Without a doubt.")
elif Answer == 4:
  print ("Magic 8 Ball :  Reply hazy, try again.")
elif Answer == 5:
  print ("Magic 8 Ball :  Ask again later.")
elif Answer == 6:
  print ("Magic 8 Ball :  Better not tell you now.")
elif Answer == 7:
  print ("Magic 8 Ball :  My sources say no.")
elif Answer == 8:
  print ("Magic 8 Ball :  Outlook not so good.")
else:
  print ("Magic 8 Ball :  Very doubtful.")

