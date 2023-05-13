import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import  pyjokes
# my name is farry
def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak somthing who you want after 5 sec ..."
              "Listening>>>....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing>>>...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand by system Please Retry>>>...")

def speech_to_text(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",120)
    engine.say(x)
    engine.runAndWait()

#speech_to_text(input("enter what you want to listen :\n typing..."))

if __name__ == '__main__':
    while True:
        print("\n speak something")
        print("Enter 2 to traverse all node values of singly linked list")
        print('Enter 3 to exit from program')
        ch = input("\nEnter your choice: ")
        if ch == '1':
            while True:
                data1 = sptext().lower()
                if "your name" in data1:
                    name = "my name is farry"
                    speech_to_text(name)
                    break

                elif "old are you" in data1:
                    age = "i am two years old"
                    speech_to_text(age)

                elif "current time" in data1:
                    time = datetime.datetime.now().strftime("%A %d. %B %Y")
                    speech_to_text(time)

                elif "do you know me" in data1:
                    know = "yes you are a legend"
                    speech_to_text(know)

                elif 'youtube' in data1:
                    webbrowser.open("https://www.youtube.com/")

                elif 'jokes' in data1:
                    joke_1 = pyjokes.get_joke(language="en", category="neutral")
                    speech_to_text(joke_1)

                elif 'exit' in data1:
                    speech_to_text("Thank you")
                    break

        elif ch == '2':
            speech_to_text("Thank you")
            break

#         elif ch == '3':
#             break
#         else:
#             print('\nWrong choice entered')
#
#
#
# #     if sptext().lower() == "lazy":
# #         while True:
#             data1 = sptext().lower()
#             if "your name" in data1:
#                 name = "my name is farry"
#                 speech_to_text(name)
#
#             elif "old are you" in data1:
#                 age = "i am two years old"
#                 speech_to_text(age)
#
#             elif "current time" in data1:
#                 time = datetime.datetime.now().strftime("%A %d. %B %Y")
#                 speech_to_text(time)
#
#             elif "do you know me" in data1:
#                 know = "yes you are a legend"
#                 speech_to_text(know)
#
#             elif 'youtube' in data1:
#                 webbrowser.open("https://www.youtube.com/")
#
#             elif 'jokes' in data1:
#                 joke_1 = pyjokes.get_joke(language="en",category="neutral")
#                 speech_to_text(joke_1)
#
#             elif 'exit' in data1:
#                 speech_to_text("Thank you")
#                 break
# else :
#     print("Thanks")
