## AI Voice Assistant – Rose
AI Voice Assistant "Rose" is a smart virtual assistant built in Python that leverages speech recognition and natural language processing to understand and respond to your voice commands. Rose can help you perform everyday tasks hands-free, such as setting reminders, answering questions, and controlling applications.

## Features
- Voice Command Recognition: Listens and processes spoken commands using speech-to-text technology.

- Natural Language Understanding: Uses OpenAI’s powerful language models to interpret and respond intelligently.

- Task Automation: Capable of setting reminders, answering questions, opening apps, and more.

- Hands-Free Interaction: Enables seamless control without typing or clicking.

- Practice with OpenAI API: Built as a learning project to practice integrating OpenAI’s API with Python.

Requirements
Python 3.7+

openai Python package

speech_recognition package

A working microphone

OpenAI API key (You need to obtain your own key from OpenAI)

Installation
Install the required Python libraries:

bash
Copy
Edit
pip install openai speechrecognition
Set your OpenAI API key as an environment variable or insert it in the script:

bash
Copy
Edit
export OPENAI_API_KEY="your_api_key_here"
Usage
Run the assistant script:

bash
Copy
Edit
python Rose.py
Speak commands clearly when prompted. Rose will listen, process your request, and respond accordingly.

Notes
This project is primarily a learning tool to practice using the OpenAI API with speech recognition.

The assistant’s capabilities depend on the quality of your microphone and your OpenAI subscription limits.

You can extend Rose by adding custom commands or integrating other APIs for more functionalities.


