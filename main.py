import pyttsx3
import googlegmail
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import time

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume',0.5)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(speachText):
	engine.say(speachText)
	engine.runAndWait()

def listen():
	r = sr.Recognizer()
	with sr.Microphone(1) as source:
		print("Say something!")
		audio = r.listen(source)

	try:
		return r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

def respond(text):
	if "messages" in text and "recent" in text:
		speak("you have "+str(googlegmail.get_unread())+" unread messages")
	elif "search" in text:
		text = text.split()
		text.pop(text.index("computer"))
		text.pop(text.index("search"))
		text = "_".join(text)
		text.strip()
		
		url = 'https://en.wikipedia.org/wiki/'+text
		r = requests.get(url)
		soup = BeautifulSoup(r.text, 'html.parser')
		result = soup.find("div", {"class":"shortdescription"})
		speak(result.text)
		
	else:
		speak("could not process you command")



text = listen()
if text:
	print(text)
	if "computer" in text:
		print("finding")
		

