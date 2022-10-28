import datetime
import pyttsx3

print("THIS IS AN ALARM AND AN TEXT TO SPEECH CONVERTOR, YOU CAN MODIFY THE TEXT YOU WANT BY CHANGING THE TEXT IN THE CODE")
speech = pyttsx3.init()
answer_1 = ("THIS IS AN ALARM AND AN TEXT TO SPEECH CONVERTOR, YOU CAN MODIFY THE TEXT YOU WANT BY CHANGING THE TEXT IN THE CODE")
speech.say(answer_1)
speech.runAndWait()

speech_1 = pyttsx3.init()
answer_2 = ("Enter the hour you want to set an alarm for: ")
speech_1.say(answer_2)
speech_1.runAndWait()
alarmHour = int(input("Enter the hour you want to set an alarm for: "))

speech_2 = pyttsx3.init()
answer_3 = ("Enter the Minutes you want to set an alarm for: ")
speech_2.say(answer_3)
speech_2.runAndWait()
alarmMin = int(input("Enter the Minutes you want to set an alarm for: "))

speech_3 = pyttsx3.init()
answer_4 = ("Enter whether its am or pm to set an alarm for: ")
speech_3.say(answer_4)
speech_3.runAndWait()
alarmAm = input("Enter whether its am or pm to set an alarm for: ")

print("Waiting for the Given Time...")
speech_5 = pyttsx3.init()
answer_6 = ("Waiting for the Given Time...")
speech_5.say(answer_6)
speech_5.runAndWait()

if alarmAm == "pm":
    alarmHour += 12
while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        text_speech = pyttsx3.init()
        print("Playing...")
        answer = ("Its already Time Bro, Come on Wake up Fast and you will be late for the College if you won't wake up, Don't blame me for not waking you up on time")
        text_speech.say(answer)
        text_speech.runAndWait()

        print("Thank you all for watching my code...")
        speech_4 = pyttsx3.init()
        answer_5 = ("Thank you all for watching my code")
        speech_4.say(answer_5)
        speech_4.runAndWait()
        break