import psutil
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.say(str(text))
    engine.runAndWait()

speak("Hello World")

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
    
while True:
    battery = psutil.sensors_battery()
    print(battery)
    print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
    if battery.percent <= 30 and battery.power_plugged == False:
        speak("Give me charge")
    
    if battery.percent >= 100:
        speak("Battery Full")
        
    time.sleep(10)