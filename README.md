# battery_percentage_speaker
This code is for windows pc, you can run this code in background and whenever your pc battery will be low or full charged, this will speak. Also you can play with code with your changes in the program.

# How to install
1. Download and Install Python
2. Install packages
    pip install psutil
    pip install pyttsx3
3. Run app.py
    python app.py 

4. If getting error for voices change the voice[0] to voice[1]
   engine.setProperty('voice', voices[1].id)
