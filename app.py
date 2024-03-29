import psutil
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 1.0)
    engine.say(str(text))
    engine.runAndWait()

speak("Hello World, I am your battery")

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

sleeptime = 60    
while True:
    battery = psutil.sensors_battery()
    print(battery)
    print("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
    if battery.percent <= 15 and battery.power_plugged == False:
        speak("Give me charge")
        sleeptime = 20
        
    if battery.percent >= 16 and battery.percent <= 97:
        sleeptime = 120
    
    if battery.percent >= 98 and battery.power_plugged == True:
        sleeptime = 20
        speak("Battery Full")
        
    time.sleep(sleeptime)