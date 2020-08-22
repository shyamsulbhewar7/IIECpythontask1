import os
import pyttsx3 as spk
import datetime
import wikipedia
import webbrowser

hour = int(datetime.datetime.now().hour)

if hour>=0 and hour<12:
   spk.speak("Good morning Sir!")
elif hour>=12 and hour<18:
   spk.speak("Good Afternoon sir!")
else :
   spk.speak("Good Evening Sir!")

spk.speak("I am jarvis sir , Please tell me how may I help you")
    

def speaker(param):
	spk.speak("I Got it sir..."+param+"...launching for you!")


while True:
	
	print("I can do following things for you sir")

	print("Do you want search something on wikipedia ?")

	print("I can open youtube for you ")

	print("I can play music for you ")

	print("I can open msedge for you sir ")

	print("I can open notepad for you ")

	print("I can open paint application for you ")

	print("I can open google for you ")

	print("I can open taskmanager for you  ")


	instr = input(" Give Your Query Here sir : ")
	if ("notepad" in instr):
		y = "notepad"
		speaker("notepad")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("calculator" in instr):
		y = "calc"
		speaker("calculator")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("youtube" in instr):
		spk.speak("Opening youtube for you sir")
		webbrowser.open("youtube.com")
	elif ("paint" in instr):
		y = "mspaint"
		speaker("Paint")
		os.system(y)
		print(y+"..LAUNCHED..")
	elif ("msedge" in instr):
		y = "msedge"
		speaker("msedge")
		os.system(y)
		print(y+"..LAUNCHED..")
	elif ("google" in instr):
		spk.speak("Opening google for you sir")
		webbrowser.open("google.com")

	elif ("taskmanager" in instr):
		y = taskmgr
		speaker("Task manager")
		os.system(y)
		print(y + "..LAUNCHED..")
	elif ("wikipedia" in instr):
		spk.speak("What you want to search on wikipedia...")
		print("Enter what you want to search :")
		question = input()
		results = wikipedia.summary(question, sentences = 4)
		spk.speak("According to wikipedia ")
		spk.speak(results)

	elif 'play music' in instr:
		musicdir = 'D:\movies\songs'
		songs = os.listdir(musicdir)
		print(songs)
		print("song started sir")
		os.startfile(os.path.join(musicdir,songs[0]))

	elif ("exit" in instr):
		y = "exit"
		spk.speak("Exiting....Come  again  sir")
		print("Exited Come Again")
		break
	else:
		spk.speak("Sorry sir , Something is wrong! Try again")
		print("Something is wrong! Try again")