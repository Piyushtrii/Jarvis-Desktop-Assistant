import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change the index for different voices

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        print("Sorry, I'm having trouble processing your request. Please try again later.")
        return "None"
    return query.lower()

def parse_command(query):
    if 'wikipedia' in query:
        return 'wikipedia'
    elif 'open youtube' in query:
        return 'open youtube'
    elif 'open google' in query:
        return 'open google'
    elif 'the time' in query:
        return 'the time'
    elif 'open code' in query:
        return 'open code'
    elif 'quit' in query or 'exit' in query:
        return 'quit'
    else:
        return 'unknown'

if __name__ == "__main__":
    try:
        import distutils
        print("Distutils is installed and available.")
    except ImportError:
        print("Distutils is not installed. Please install it using 'python -m ensurepip --upgrade' or 'pip install setuptools'.")
    
    wish_me()
    while True:
        query = take_command()

        if query == "None":
            continue

        command = parse_command(query)

        if command == 'wikipedia':
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results. Please be more specific.")
                print("Wikipedia DisambiguationError:", e)
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I could not find any relevant page.")
                print("Wikipedia PageError:", e)
            except Exception as e:
                speak("Sorry, I encountered an error while searching Wikipedia.")
                print("Wikipedia Error:", e)

        elif command == 'open youtube':
            webbrowser.open("https://www.youtube.com")

        elif command == 'open google':
            webbrowser.open("https://www.google.com")

        elif command == 'the time':
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif command == 'open code':
            code_path = "C:\\Path\\To\\Your\\CodeEditor.exe"  # Change this to your code editor's path
            os.startfile(code_path)

        elif command == 'quit':
            speak("Goodbye!")
            break

        else:
            speak("Unknown command. Please try again.")
            print("Unknown command. Please try again.")
