import random

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
takenspots = []

playerpoints = 0
AIpoints = 0

pieces = ["X", "O"]	
playerpiece = random.choice(pieces)
if playerpiece == "X":
	AIpiece = pieces[1]
else:
	AIpiece = "X"
print("Your piece is", playerpiece, "!")

def gameboard():
	for row in range(3):
		for line in range(3):
			print("|__"+list[row*3+line]+"__|__", end="")
		print()
	return list

def reset():
	takenspots.clear()
	for row in range(3):
			for line in range(3):
				print("|__"+list[row*3+line]+"__|__", end="")
			print()


def playerchoices():
	print(gameboard())
	userinput = input("Pick a spot on the board!: ")
	for x in range(len(list)):
		if list[x] == userinput:
			list[x] = playerpiece
			takenspots.append(userinput)
	print(gameboard())
	print()


def AIchoices():
#needs to block player 30% of time -- if not blocking, it's doing this: 
	if list[4] == "e":
		list[4] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] == "a":
		list[0] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] == "c":
		list[2] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] != "c" and list[6] == "g":
		list[6] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] != "c" and list[6] != "g" and list[8] == "i":
		list[8] = AIpiece
		print(gameboard())
	elif list[1] != "e" and list[0] != "a" and list[2] != "c" and list[6] != "g" and list[8] != "i" and list[1] == "b":
		list[1] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] != "c" and list[6] != "g" and list[8] != "i" and list[1] != "b" and list[3] == "d":
		list[3] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] != "c" and list[6] != "g" and list[8] != "i" and list[1] != "b" and list[3] != "d" and list[5] == "f":
		list[5] = AIpiece
		print(gameboard())
	elif list[4] != "e" and list[0] != "a" and list[2] != "c" and list[6] != "g" and list[8] != "i" and list[1] != "b" and list[3] != "d" and list[5] != "f" and list[7] == "h":
		list[7] = AIpiece
		print(gameboard())


def winconditions():
	if list[0] == playerpiece and list[1] == playerpiece and list[2] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[0] == AIpiece and list[1] == AIpiece and list[2] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#middle row
	if list[3] == playerpiece and list[4] == playerpiece and list[5] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[3] == AIpiece and list[4] == AIpiece and list[5] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#bottom row 
	if list[6] == playerpiece and list[7] == playerpiece and list[8] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[6] == AIpiece and list[7] == AIpiece and list[8] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#first column
	if list[0] == playerpiece and list[3] == playerpiece and list[6] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[0] == AIpiece and list[3] == AIpiece and list[6] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#second column
	if list[1] == playerpiece and list[4] == playerpiece and list[7] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[1] == AIpiece and list[4] == AIpiece and list[7] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#third column
	if list[2] == playerpiece and list[5] == playerpiece and list[8] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[2] == AIpiece and list[5] == AIpiece and list[8] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#diagnol from top left
	if list[0] == playerpiece and list[4] == playerpiece and list[8] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[0] == AIpiece and list[4] == AIpiece and list[8] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())
	#diagnol from top right
	if list[2] == playerpiece and list[4] == playerpiece and list[6] == playerpiece:
		playerpoints += 1 
		print(playerpoints, AIpoints)
		print(reset())
	elif list[2] == AIpiece and list[4] == AIpiece and list[6] == AIpiece:
		AIpoints += 1
		print(playerpoints, AIpoints)
		print(reset())

def gameloop():
	while playerpoints < 3 and AIpoints < 3:
		for i in range(30):
			playerchoices()
			winconditions()
			if playerpoints == 3 or AIpoints == 3:
				break 
			AIchoices()
			winconditions()
			if playerpoints == 3 or AIpoints == 3:
				break 
	if playerpoints == 3:
		print("You win!")
	elif AIpoints == 3:
		print("You lost!")

def main():
	print(gameloop())

main()
