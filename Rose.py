import queue
import sounddevice as sd
import json
import pyttsx3
import openai
import subprocess
import speech_recognition as sr
import threading
import time
from vosk import Model, KaldiRecognizer

# OpenAI key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Text-to-speech
engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Daniel')  # Jarvis-like British male
engine.setProperty('rate', 150)

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

# Load Vosk model
model = Model("model")
recognizer = KaldiRecognizer(model, 16000)
q = queue.Queue()

# Vosk wake word detection (runs in background)
def listen_background():
    def callback(indata, frames, time_info, status):
        if recognizer.AcceptWaveform(indata):
            result = json.loads(recognizer.Result())
            if result.get("text"):
                q.put(result["text"])

    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening for wake word 'Jarvis'...")
        while True:
            sd.sleep(1000)

# OpenAI GPT response
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Simple command handler
def handle_command(command):
    command = command.lower()
    if "time" in command:
        speak("It is " + time.strftime("%I:%M %p"))
    elif "open chrome" in command:
        subprocess.call(["open", "-a", "Google Chrome"])  # macOS only
    elif "shutdown" in command:
        speak("Goodbye, sir.")
        exit()
    else:
        speak("Thinking...")
        response = ask_openai(command)
        speak(response)

# Main loop
def main():
    speak("Jarvis is online and standing by.")
    threading.Thread(target=listen_background, daemon=True).start()

    while True:
        phrase = q.get().lower()
        print(f"Heard: {phrase}")
        if "jarvis" in phrase:
            speak("Yes sir?")
            try:
                recognizer = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio)
                print(f"You said: {command}")
                handle_command(command)
            except Exception as e:
                speak("Sorry, I didn’t catch that.")

if __name__ == "__main__":
    main()

