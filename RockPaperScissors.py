print("Welcome to the game\n")
inputtest = ["R","P","S"]
Name1 = input("Enter name for Player1\n")
Name2 = input("Enter name for Player2\n")
point1 = 0
point2 = 0
gp = "Y"
while ((gp == "Y")|(gp=="y")):
    p1 = input("Name1 enter R for Rock or P for Paper or S for Scissor\n")
    p2 = input("Name2 enter R for Rock or P for Paper or S for Scissor\n")
    if (p1 not in inputtest)&(p2 not in inputtest):
        print("Oops! Invalid entry. Play again\n")
        continue
    if(p1==p2):
        print("That's a tie. Play again\n")
        continue
    if(((p1=="R")&(p2=="S"))|((p1=="S")&(p2=="P"))|(p1=="P")|(p2=="R")):
        print(Name1," wins\n")
        point1= point1 + 1
    else:
        print(Name2," wins\n")
        point2 = point2 + 1
    gp = input("Type Y to play again. If you want to exit type any other key\n")
    if ((gp != "y")&(gp != "Y")):
        PointsTable = {Name1: point1, Name2: point2}
        print("The results of the game are\n", Name1, " has ",PointsTable[Name1], " points\n", Name2, " has ", PointsTable[Name2], " points ")
    else:
        continue
