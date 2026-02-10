import pyttsx3

engine = pyttsx3.init()

age = int(input("your enter age"))

if age >= 18:
    engine.say("You are eligible")
else:
    engine.say("You are not eligible")

engine.runAndWait()
