# Introduction

This is a very interesting, tricky, confusing, and difficult project which I have decided to work on. A YouTube video Q&A chatbot is a bot that gives answers to the questions asked regarding a video over at YouTube. Look at the "Instructions" section to understand how it works.

## Instructions

At the start of the program, you will be asked to enter a YouTube URL so that it can download its audio file and transcribe it to get the text from the video with the help of OpenAi's Whisper. After transcribing, you will have the chance to ask a question regarding that video's content.\
NOTE: Be careful when using a video as it can only transcribe audio files that don't exceed the 25 MB limit as per Whisper's requirements.

To get started, you need to have these libraries and modules downloaded and installed:
- openai.
- faiss-cpu.
- moviepy.
- pytube3.
- langchain.
- tiktoken.\

You can install them all through pip:
```
pip install openai faiss-cpu moviepy pytube3 langchain tiktoken
```
You will also need your OpenAI API key to enter it where there's an empty string inside the code:
```
os.environ["OPENAI_API_KEY"] = ""
```

### This is an active project and there can be problems that might occur. The program will improve along with my knowledge of AI, Python, and such.
