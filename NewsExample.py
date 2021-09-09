import requests
import os
import pickle
import time
os.system("spd-say 'Hello world'")
r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=05719232b9d94c3294a638b67f2584f1")
url="https://newsapi.org/v2/top-headlines?country=us&apiKey=05719232b9d94c3294a638b67f2584f1"
data={"p1":4,"p2":8}
#re=requests.post(url,data)
ls=[[x] for x in r.text.splitlines()]
f1=open("File.txt","wb")
pickle.dump(ls,f1)
f1.close()
f1=open("File.txt","rb")
content=pickle.load(f1)
os.system(f"spd-say{content}")
