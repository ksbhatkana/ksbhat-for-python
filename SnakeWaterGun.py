#Author: KS Bhat
import random
i=0
choices=["S","W","G"]
score1=0
score2=0
print("="*25,"\nSnake wins over Water\nGun wins over Snake\nWater wins over Gun\n"+"="*25)
print("Enter your name:")
user=input()
while i<=10:
        ch1=random.choice(choices)
        print("\nEnter your choice\n1.S for Snake\n2.W for Water\n3.G for Gun")
        ch2=input()
        ch2=ch2.upper()
        if(ch1==ch2):
                print("You both chose same....Be smart next time")
                i+=1
        elif(ch1=="S" and ch2=="W"):
                score1+=1
                i+=1
                print("Computer scores over you as it chose Snake..Water is in Snake's Belly\nComputer score: ",score1,"\nYour score: ",score2)
        elif(ch1=="W" and ch2=="S"):
                score2+=1
                i+=1
                print("You score over Computer as Computer chose Snake..Water is in Snake's Belly\nComputer score: ",score1,"\nYour score: ",score2)
        elif(ch1=="G" and ch2=="S"):
                score1+=1
                i+=1
                print("Computer scores over you as it chose Gun..Snake is dead\nComputer score: ",score1,"\nYour score: ",score2)
        elif(ch1=="S" and ch2=="G"):
                score2+=1
                i+=1
                print("You score over Computer as Computer chose Snake..Snake is dead\nComputer score: ",score1,"\nYour score: ",score2)
        elif(ch1=="W" and ch2=="G"):
                score1+=1
                i+=1
                print("Computer scores over you as he chose Water..Gun may not work,bcz water spoiled it\nComputer score: ",score1,"\nYour score: ",score2)
        elif(ch1=="G" and ch2=="W"):
                score2+=1
                i+=1
                print("You score over Computer as it chose Gun..Gun may not work,bcz water spoiled it\nComputer score: ",score1,"\nYour score: ",score2)
        else:
                print("Ohh!Wrong Input\nGo through rules again\n")
print("\n\n\n\nFinal scores are\nComputer: "+str(score1)+"\nYou: ",str(score2))
if score1>score2:
        print("It's a clear victory for Computer")
elif score2>score1:
        print("It's a clear victory for champ",user)
else:
        print("You both are equally strong")                   
