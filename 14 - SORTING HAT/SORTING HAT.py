Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print ("Q1) Do you like Dawn or Dusk ?")
print ("  1) Dawn")  
print ("  2) Dusk")

answer_1 = int(input("Choose between option 1-2: "))

if answer_1 == 1:
  Gryffindor +=1
  Ravenclaw +=1
elif answer_1 == 2:
  Hufflepuff +=1
  Slytherin +=1
else:
  print ("Wrong Input, Please choose between option 1 & 2")

print ("\n Q2) When I'm dead, I want people to remember me as :")
print ("  1) The Good")
print ("  2) The Great")
print ("  3) The Wise")
print ("  4) The Bold")


answer_2 = int(input("Choose option between 1 & 4 : "))

if answer_2 == 1:
  Hufflepuff +=2
elif answer_2 ==2:
  Slytherin +=2
elif answer_2 ==3:
  Ravenclaw +=2
elif answer_2 ==4:
  Gryffindor +=2
else:
  print("Wrong Input.")

print ("\n Q3) Which kind of instrument most pleases your ear ?")
print ("  1) The Violin")
print ("  2) The Trumpet")
print ("  3) The Piano")
print ("  4) The Drum")

answer_3 = int(input("Choose between option 1 & 4 : "))

if answer_3 ==1:
  Slytherin +=4
elif answer_3 ==2:
  Hufflepuff +=4
elif answer_3 ==3:
  Ravenclaw +=4
elif answer_3 ==4:
  Gryffindor +=4
else:
  print ("Wrong Input.")

print ("\n House Scores : ")
print ("\n🦁 Gryffindor" , Gryffindor)
print ("🐍 Slytherin" , Slytherin)
print ("🦡 Hufflepuff" , Hufflepuff)
print ("🦅 Ravenclaw" , Ravenclaw)


# Bonus BCZ I am a POTTERHEAD

print ("\n SORTING HAT :  WHICH HOUSE YOU WANNA GET INTO ?")
print ("  1) Gryffindor")
print ("  2) Slytherin")
print ("  3) Hufflepuff")
print ("  4) Ravenclaw")

answer_4 = int(input("\nChoose a house you want for yourself , Because SORTING HAT cares about your opinion too . Make sure to choose betwen Option 1 & 4 : "))

if answer_4 ==1:
  print ("SORTING HAT :  🦁GRYFFINDOR")
elif answer_4 ==2:
  print ("SORTING HAT :  🐍SLYTHERIN")
elif answer_4 ==3:
  print ("SORTING HAT :  🦡HUFFLEPUFF")
elif answer_4 ==4:
  print ("SORTING HAT :  🦅RAVENCLAW")
else:
  print ("WRONG INPUT")
