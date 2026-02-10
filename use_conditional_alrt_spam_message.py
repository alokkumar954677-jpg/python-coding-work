import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',100)
voices=engine.getProperty('voices')
engine.setProperty('volume',0.8)
engine.setProperty('voice',voices[1].id)

m1="free"
m2="win / winner"
m3="congratulations"
m4="urgent Limited offer"
m5="click here"
m6="claim now"
m7="100 guaranteed"
m8="earn money fast"
m9="no investment"
m10="lottery"
m11="cash prize"
message=input("enter your comment=")
if(m1 in message or m2 in message or m3 in message or m4 in message or m5 in message or m6 in message or m7 in message or m8 in message or m9 in message or m10 in message or m11 in message):
    engine.say("this message is spam not click here link")
else:
    engine.say("not spam use here link")
engine.runAndWait()
