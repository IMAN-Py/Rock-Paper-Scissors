print ("programmer : IMAN_TB")
print ("Email : mtmimana@gmail.com")
import random
point = 0
while(True):
	print("point : " +str(point))
	selection = input("1- Rock \n2- Paper  \n3- Scissors \n")
	selection = int(selection)
	if selection == 0 : 
		break
	if (selection != 1) and (selection != 2) and (selection != 3):
		print("Invalid input !!")
		break
	Systemselection = random.randint(1,3)
	Systemselectionstaring = ""
	if Systemselection == 1 : Systemselectionstaring = "Rock"
	elif Systemselection == 2 : Systemselectionstaring = "Paper"
	elif Systemselection == 3 : Systemselectionstaring = "Scissors"
	print("System selection : "+Systemselectionstaring)
	if(Systemselection == 1 and selection == 2) or (Systemselection == 2 and selection == 3) or (Systemselection == 3 and selection == 1):
		print("You Win !!!")
		point+=1
	elif Systemselection == selection :
		print("Was equal !!")
	else :
		print("You lost !!!")
		point-=1
	print("\n\n")




quit = input()

