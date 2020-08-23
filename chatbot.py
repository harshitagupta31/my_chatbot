from chatterbot import ChatBot
import nltk
from nltk.chat.util import Chat,reflections 
from chatterbot.trainers import ListTrainer
from tkinter import*
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()

    
bot= ChatBot("my bot")
convo=['hi','hello',
'what is your name?','my  name  is  bot,  created   by   harshita',
'how r u?','fine',
'where do u live?','in   bareilly',
'which language do u speak?','english   mainly',
'safety measures of corona','washimg   your   hand   &    social distancing',
'when this lockdown will get over?','only   modi   ji   can   give   this   ans',
'who is dog?','harsh  doggy',
'mom love the most','kimi',
'who is kali?','navisha',
'who is thali ka baigan?','avani    mittal',]

trainer=ListTrainer(bot)
#training the bpot by trainer
trainer.train(convo)
#ans = bot.get_response('mom love the most')
#print(ans)
#print('talk to bot')
#while True:
    #question=input()
    #if question=='exit':
     #   break
    #answer=bot.get_response(question)
   # print("bot :", answer)'
#for windows pyttsx3 2.71
main = Tk()
main.geometry("500x650")
main.title("My Chat Bot")
img=PhotoImage(file="C:\\Users\\HARSHITA GUPTA\\Documents\\robot.png")
photo=Label(main,image=img)
photo.pack(pady=10)


#fun for speaker and convert audio into string
def  takequest():
    sr=s.Recognizer()
    sr.pause_threshold=0
    print("bot is listening")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            question =sr.recognize_goggle(audio,language='eng-in')
            text.delete(0,END)
            text.insert(0,question)
            ask_from_bot()
        except Exception as e:
             print(e)
    

def ask_from_bot():
    question=text.get()
    answer_from_bot=bot.get_response(question)
    msgs.insert(END,"you :" +question)
    msgs.insert(END,"bot :" +str(answer_from_bot))
    speak(answer_from_bot)
    text.delete(0,END)
    msgs.yview(END)

    
frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text field
text=Entry(main,font=("Verdana",20))
text.pack(fill=X,pady=10)
btn=Button(main, text="Ask from bot", font=("Verdana", 20),command=ask_from_bot)
btn.pack()

#creating a func
def enter_function(event):
    btn.invoke()
#bind main window with enter key
main.bind('<Return>',enter_function)
def repeat():
    while True:
        takequest()
t=threading.Thread(target=repeat)
t.start()
main.mainloop()   
