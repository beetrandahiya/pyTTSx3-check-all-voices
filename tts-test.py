import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)                                                     #you can change the rate here
for voice in voices:
    print(voice)
    engine.setProperty('voice',voice.id)
    engine.say("Hello, This is the voice you'll hear if you choose me.")       #here goes the text you want to hear as a test
    engine.runAndWait()
