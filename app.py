import os
import pyttsx3
import speech_recognition as sr

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return command.lower()

def is_app_running(app_name):
    try:
        tasklist = os.popen('tasklist').read().lower()
        return app_name.lower() in tasklist
    except Exception:
        return False

def open_application(app_name):
    if app_name == "notepad":
        os.system("start notepad.exe")
        speak("Notepad opened.")
    elif app_name == "calculator":
        os.system("start calc.exe")
        speak("Calculator opened.")
    elif app_name == "store":
        os.system("start ms-windows-store:")
        speak("Microsoft Store opened.")
    elif app_name == "word":
        os.system("start winword")
        speak("Microsoft Word opened.")
    elif app_name == "excel":
        os.system("start excel")
        speak("Microsoft Excel opened.")
    elif app_name == "powerpoint":
        os.system("start powerpnt")
        speak("Microsoft PowerPoint opened.")
    elif app_name == "camera":
        os.system("start microsoft.windows.camera:")
        speak("Camera opened.")
    elif app_name in ["browser", "chrome"]:
        if not is_app_running("chrome.exe"):
            chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            os.startfile(chrome_path)
            speak("Google Chrome opened.")
        else:
            speak("Google Chrome is already running.")
    elif app_name == "spotify":
        os.system("start spotify:")
        speak("Spotify opened.")
    elif app_name == "whatsapp":
        os.system("start whatsapp:")
        speak("WhatsApp opened.")
    else:
        # If the application is not found in the list, open the browser and search for it
        search_query = app_name.replace(" ", "+")
        os.system(f'start microsoft-edge:https://www.bing.com/search?q={search_query}')
        speak(f"Searching for {app_name} on Microsoft Edge.")

def close_application(app_name):
    if app_name == "notepad":
        os.system("taskkill /f /im notepad.exe")
        speak("Notepad closed.")
    elif app_name == "calculator":
        os.system("taskkill /f /im calculator.exe")
        speak("Calculator closed.")
    elif app_name == "store":
        os.system("taskkill /f /im WinStore.App.exe")
        speak("Microsoft Store closed.")
    elif app_name == "word":
        os.system("taskkill /f /im WINWORD.EXE")
        speak("Microsoft Word closed.")
    elif app_name == "excel":
        os.system("taskkill /f /im EXCEL.EXE")
        speak("Microsoft Excel closed.")
    elif app_name == "powerpoint":
        os.system("taskkill /f /im POWERPNT.EXE")
        speak("Microsoft PowerPoint closed.")
    elif app_name == "camera":
        os.system("taskkill /f /im WindowsCamera.exe")
        speak("Camera closed.")
    elif app_name in ["browser", "chrome"]:
        os.system("taskkill /f /im chrome.exe")
        speak("Google Chrome closed.")
    elif app_name == "spotify":
        os.system("taskkill /f /im Spotify.exe")
        speak("Spotify closed.")
    elif app_name == "whatsapp":
        os.system("taskkill /f /im WhatsApp.exe")
        speak("WhatsApp closed.")
    else:
        speak("I didn't understand that application. Please try again.")

def main():
    speak("Welcome, sir. How can I assist you today?")
    
    while True:
        command = take_command()

        if command == "none":
            continue

        if "open" in command:
            app_name = command.replace("open", "").strip()
            open_application(app_name)
        elif "close" in command:
            app_name = command.replace("close", "").strip()
            close_application(app_name)
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye, sir.")
            print("Exiting.")
            break

if __name__ == "__main__":
    main()
