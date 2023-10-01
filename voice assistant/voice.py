import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyjokes
import pyautogui
import tkinter as tk
from PIL import Image, ImageTk
from translate import Translator

# Initialize the Text-to-Speech engine
engine = pyttsx3.init('sapi5')

# Translator object for translation
T = Translator(from_lang="English", to_lang="Hindi")

# Function to speak a given text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to take a screenshot
def screenshot():
    pic = pyautogui.screenshot()
    pic.save('screenshot.png')

# Function to greet the user based on the time
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 6:
        speak("Hey Owl")
    elif 6 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Hello sir")
    speak("I'm your Personal Voice Assistant. Please tell me how may I help you?")

# Function to recognize user's voice command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return query

# Function to send an email
def sendEmail(to, content):
    server = smtplib.SMTP('nandhinibharanidharan22@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nandhinibharanidharan22@gmail.com', '')
    server.sendmail('nandhinibharanidharan9@gmail.com', to, content)
    server.close()

# Function to tell a joke
def joke():
    speak(pyjokes.get_joke(language='en', category='all'))

# Main function for voice assistant functionality
def main():
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)
            print(results)

        elif 'open  college website' in query:
            webbrowser.open("https://www.psgcas.ac.in/")

        elif 'start youtube' in query:
            webbrowser.open("https://www.youtube.com")

        # Add more commands for opening websites or applications

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to omkar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourgmail@gmail.co"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'shutdown' in query:
            print("Shutting down...")
            speak("Shutting down")
            quit()

        elif 'translate' in query:
            query = query.replace('translate', '')
            translation = T.translate(query)
            speak(translation)
            print(translation)

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        # Add more custom commands as needed

# Function to create the GUI
def create_gui():
    root = tk.Tk()
    root.title("Voice Assistant")
    root.geometry("700x600")

    # Load and process the GIF frames
    gif_frames = []
    gif_path = r"C:\Users\hp\Music\voice assistant\ass.gif"
    gif = Image.open(gif_path)
    gif_width, gif_height = gif.size

    for frame in range(gif.n_frames):
        gif.seek(frame)
        frame_image = gif.copy().resize((gif_width, gif_height), Image.LANCZOS)
        frame_photo = ImageTk.PhotoImage(frame_image)
        gif_frames.append(frame_photo)

    # Display the GIF frames on a label widget
    gif_label = tk.Label(root)
    gif_label.pack()

    def update_gif(frame_index):
        frame_photo = gif_frames[frame_index]
        gif_label.config(image=frame_photo)
        gif_label.image = frame_photo
        frame_index = (frame_index + 1) % len(gif_frames)
        root.after(100, update_gif, frame_index)

    # Start updating the GIF frames
    update_gif(0)

    lbl1 = tk.Label(root, text="Welcome to Voice Assistant App\n", wraplength=300)
    lbl1.pack()

    but1 = tk.Button(root, text="Run the Assistant", command=main)
    but1.pack(padx=10, pady=10)

    quit4 = tk.Button(root, text="EXIT", command=root.destroy)
    quit4.pack(padx=10, pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
