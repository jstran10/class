import random
x=random.randint(0,3)
repeat=True
ar=["rock","paper","scissors"]
while repeat==True:
	rps=input("rock, paper, or scissors\n")
	print("You chose: "+rps+"\n")
	comp=ar[random.randint(0,2)]
	print("Computer chose: "+comp+"\n")
	if rps==comp:
		print("Try again\n")
	else:
		repeat=False
		if (rps=="rock" and comp=="scissors") or (rps=="paper" and comp=="rock") or (rps=="scissors" and comp=="paper"):
			print("You Win")
		else:
			print("You Lose")
	


