f1=open("File.txt","w")
f1.write("Raj\nKamal\nHero\nRamesh\nSuraj\nAnjan\nBaby\nChethu\nDeeko\nEesh\nFaki\nGowindd\nHarish\nIdor\nJayant")
f1.close()
f1=open("File.txt","r")
def searchFile():
        while True:
                content=f1.read()
                
                text=(yield)
                if text in content:
                        print("Your name found")
                else:
                        print("Don't worry, we're still searching")
        else:
                print("Sorry, you're not on list")
if __name__=='__main__':
        print("Enter your name")
        name=input()
        searchHere=searchFile()
        next(searchHere)
        searchHere.send(name)
        searchHere.close()
        f1.close()
