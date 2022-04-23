from os import remove
from winsound import PlaySound
import requests
import speech_recognition as sr     
import subprocess
from gtts import gTTS
import playsound



bot_message = ""
message=""

r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message, lang="vi", slow=False)
myobj.save("welcome.mp3")
print('saved')

playsound.playsound('welcome.mp3', True)
remove('welcome.mp3')

while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Speak Anything :")
        audio = r.listen(source)  
        try:
            message = r.recognize_google(audio,language="vi-VI")  
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice") 
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5005/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message, lang="vi", slow=False)
    myobj.save("welcome.mp3")
    print('saved')
    playsound.playsound('welcome.mp3', True)
    remove("welcome.mp3")