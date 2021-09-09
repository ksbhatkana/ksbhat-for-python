'''import time
import vlc
print("Hey Programmer!!You don't worry, I'll take care of your help:)")
print("Are you there ?")
ch=input()
water=3.5
f1=open("Water.txt","w")
f2=open("EyeEx.txt","w")
f3=open("BodyEx.txt","w")
if(ch=='y' or ch=='Y'):
        i=9
        i2=30
        j1=9
        j2=45
        k1=9
        k2=45
        while True:
                hour1=time.localtime().tm_hour
                minute1=time.localtime().tm_min
                if(hour1==i and minute1==i2):
	                print("Time for water")
	                f1=open("Water.txt","a")
	                f1.write("-"*20)
	                time1=date.date()
	                f1.write(time1)
	                media=vlc.MediaPlayer("Water.mp3")
	                media.play()
	                time.sleep(500)
	                media.stop()
                if(hour1==j1 and minute1==j2):
	                print("Time for Eye excercise")
	                f2=open("EyeEx.txt","a")
	                f2.write("-"*20)
	                time2=date.date()
	                f2.write(time2)
                if(hour1==k1 and minute1==k2):
	                print("Time for Body excercise")
	                f3=open("BodyEx.txt","a")
	                f3.write("-"*20)
	                time3=date.date()
	                f3.write(time3)
                minute2=minute1+45
	        minute3=minute1+30
	        minute4=minute1+45''
                i2=i2+1
                j2=j2+45
                k2=k2+45
                if(i2/60>=1):
                        i=i2//60
                        i2=i2%60
                elif(j2/60>=1):
                        j1=j2//60
                        j2=j2%60
                elif(k2/60>=1):
                        k1=k2//60
                        k2=k2%60
f1.close()
f2.close()
f3.close()'''


























import pygame
import datetime
import time
def musiconloop(filee,stopper):
	mixer.init()
	mixer.music.load(filee)
	mixer.music.play()
	while True:
		a=input()
		if a==stopper:
			mixer.music.stop()
			break
def log_now(msg):
	f=open("mylogs.txt","a")
	f.write(f"{msg}" {datetime.now()}\n")
if __name__=='__main__':
	init_water=time()
	init_eyes=time()
	init_exercise=time()
	watersecs=5
	exsecs=10
	eyesecs=20
	while True:
		if time()-init_water>watersecs:
			print("Water Drinking time. Enter 'drank' to stop the alarm."
			musiconloop("water.mp3","drank")
			init_water=time()
			log_now("Drank water at")
		if time()-init_eyes>eyesecs:
			print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
			musiconloop("eyes.mp3","doneeyes")
			init_eyes=time()
			log_now("Eye exercise at")
		if time()-init_exercise>exesecs:
			print("Physical Activity time. Enter 'donephy' to stop the alarm."
			musiconloop("physical.mp3","donephy")
			init_exercise=time()
			log_now("Physical Activity at")
