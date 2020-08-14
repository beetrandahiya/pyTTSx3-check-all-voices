import pyttsx3
engine = pyttsx3.init()
test_txt=input("Enter the text you want to hear")
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)                                                     #you can change the rate here
for voice in voices:
    print(voice)
    engine.setProperty('voice',voice.id)
    engine.say(test_txt)       
    engine.runAndWait()
