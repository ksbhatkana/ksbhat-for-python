import os
import re
def funn(path,file1,file2):
	os.chdir(path)
	f1=open(file1)
	f2=open(file2)
	contentf2=f2.read()
	j=1
	for i in os.listdir():
		print(i)
		print(contentf2)
		namei,ext=i.split('.')
		ext='.'+ext
		if ext==contentf2:
			print(i)
			new=f"{str(j).contentf2}"
			os.rename(i,new)
			j+=1
		else:
			print("Hi")
	contentf1=list(f1.read())
	'''for f in contentf1:
		neww=f"{f.capitalize()}"
		os.rename(f,neww)'''
	f1.close()
	f2.close()
funn("/home/ksbhat/Desktop/Python Fun/Hi","hi.txt","hi2.txt")
