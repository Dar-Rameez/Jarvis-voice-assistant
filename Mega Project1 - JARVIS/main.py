import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def find_application(app_name):
    # Directories to search for installed applications
    search_dirs = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        r"C:\Users\darsa\AppData\Local\Programs"  # Common path for user-installed apps
    ]
    
    for dir in search_dirs:
        for root, dirs, files in os.walk(dir):
            for file in files:
                if file.lower().startswith(app_name.lower()) and file.endswith(".exe"):
                    return os.path.join(root, file)
    return None

def processCommand(c):
    command = c.lower()

    # Open web applications
    if "open google" in command:
        webbrowser.open("https://google.com")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")

    # Open specific local system applications
    elif "open word" in command:
        subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')  # Adjust path as per your version

    elif "open excel" in command:
        subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')  # Adjust path as per your version

    elif "open powerpoint" in command:
        subprocess.Popen(r'C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE')  # Adjust path as per your version

    elif "open command prompt" in command or "open cmd" in command:
        subprocess.Popen("cmd.exe")

    elif "open file explorer" in command:
        subprocess.Popen("explorer.exe")

    elif "open edge" in command:
        subprocess.Popen(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')  # Path for Microsoft Edge

    elif "open whatsapp" in command:
    # This opens the Microsoft Store version of WhatsApp
    # Using the AppID you found for WhatsApp
        subprocess.Popen(["powershell", "Start-Process shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])

        
    # Dynamic application search for other applications
    elif "open" in command:
        app_name = command.replace("open ", "").strip()
        app_path = find_application(app_name)
        if app_path:
            subprocess.Popen(app_path)
            speak(f"Opening {app_name}")
        else:
            speak(f"Sorry, I couldn't find {app_name} installed on your system.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening ")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Error; {e}")
