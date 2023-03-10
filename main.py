"""
Modules:

openai = Allows access to ChatGPT functions. 
os = Allows the program to use terminal and system functions. 
speech_recognition = Allows access to text-to-speech and speech-to-text for input and output.
gtts = N/A
"""
import os
import subprocess
import sys
import time
import threading

def installing_animation(time_to_wait):
    animation = "|/-\\"
    idx = 0
    while time_to_wait > 0:
        print("Installing " + animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        time_to_wait -= 0.1
    print("This installation has finished.")
    
def loading_animation(time_to_wait):
    animation = "|/-\\"
    idx = 0
    while time_to_wait > 0:
        print("Loading " + animation[idx % len(animation)], end="\r")
        idx += 1
        time.sleep(0.1)
        time_to_wait -= 0.1
    print("Successfully loaded!")

def installationrequirements():
    print("Please wait while we download the required packages.")
    installreqs = subprocess.run(
        [
            "pip", 
            "install", 
            "--target=C:\\Users\\kiera\\Desktop\\ChatGPT_v2\\ChatGPT\\Lib\\site-packages", 
            "openai", 
            "SpeechRecognition", 
            "gtts"
        ], 
        capture_output=True)
    if installreqs.returncode == 0:
        installoutput = installreqs.stdout.decode('utf-8')
        print(installoutput)
    else:
        installerror = installreqs.stderr.decode('utf-8')
        print('Error:', installerror)

thread2 = threading.Thread(target=installationrequirements)

def installationadditionals():
    print("Please wait while we install the additional packages. This may take a few minutes.")
    installadditonals = subprocess.run(
        [
        "pip", 
        "install", 
        "--target=C:\\Users\\kiera\\Desktop\\ChatGPT_v2\\ChatGPT\\Lib\\site-packages", 
        "openai[embeddings]", 
        "openai[wandb]", 
        "openai[datalib]",
        "pyaudio"
        ], 
        capture_output=True)
    if installadditonals.returncode == 0:
        installadditonalsoutput = installadditonals.stdout.decode('utf-8')
        print(installadditonalsoutput)
    else:
        installadditionalerror = installadditonals.stderr.decode('utf-8')
        print('Error:', installadditionalerror)

thread3 = threading.Thread(target=installationadditionals)
            
def installation():
    thread2.start()
    thread3.start()

sys.path.append("C:\\Users\\kiera\\Desktop\\ChatGPT_v2\\ChatGPT\\Lib\\site-packages")

import openai
import speech_recognition as sr
from gtts import gTTS

# Requests the user's API Key.
openai.api_key = input("What is your API Key? ")

# Set up OpenAI API credentials
openai.api_key = os.environ

# Runs a API Key Test via the api_key.py program.
def akt():
    apikeytest = subprocess.run(['python', '/workspaces/codespaces-blank/ChatGPTAI/utils/apikeytest.py'], capture_output=True)
    if apikeytest.returncode == 0:
        # Get the stdout output of the subprocess
        output = apikeytest.stdout.decode('utf-8')
        print(output)

    else:
        error = apikeytest.stderr.decode('utf-8')
        print('Error:', error)

loading_animation(5)

# Create a recognizer object
r = sr.Recognizer()

# Capture speech from the microphone
def get_audio():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
        text = prompt
    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

get_audio()

# Generate speech from text
def speak(text):
    tts = gTTS(text)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

# Send a prompt to ChatGPT and receive a response
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

# Main loop
while True:
    # Get user input
    prompt = get_audio()
    
    # Check if user said "bye"
    if prompt and "bye" in prompt:
        speak("Goodbye!")
        break
    
    # Get response from ChatGPT
    response = get_response(prompt)
    
    # Speak the response
    speak(response)
