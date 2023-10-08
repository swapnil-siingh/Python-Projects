'''Rock Paper Scissor Game''' 
import random

a = random.randint(1,  3)


if a==1:
	comp='r'
elif a==2:
	comp='p'
else:
	comp='s'


you=input("Player's Turn : Rock(r) Paper(p) Scissor(s) \n")	

victory=None
if comp==you:
	print("Tie Match")
elif comp=='r':
	if you=='p':
		victory=True
	else:
		victory=False
elif comp=='p':
	if you=='s':
		victory=True
	else:
		victory=False
else:
	if you=='r':
		victory=True
	else:
		victory=False	

if comp=='r':
	print("Computer Selected Rock")
if comp=='p':
	print("Computer Selected Paper")
if comp=='s':
	print("Computer Selected Scissor")



if victory==True:
	print("You Won!!")
elif victory==False:
	print("Computer Won")
	