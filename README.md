# Jarvis Desktop Assistant

## Overview
The ** Jarvis Desktop Assistant** is a Python-based project that serves as a voice-controlled personal assistant capable of performing various tasks. 
These include opening websites, providing the current time, playing music, capturing photos using the webcam, and managing files and folders on the user's system. 
The project utilizes several Python libraries to deliver an interactive and feature-rich experience.

## Features
1. **Speech Recognition**:
   - Uses the `speech_recognition` library to process voice commands.
   - Recognizes commands in English (India) using Google's Speech Recognition API.

2. **Text-to-Speech**:
   - Uses the `pyttsx3` library to provide voice responses to user commands.

3. **Web Navigation**:
   - Opens popular websites like Google, YouTube, Facebook, Instagram, and others using the `webbrowser` module.

4. **Time Announcement**:
   - Provides the current time in `HH:MM:SS` format.

5. **Music Playback**:
   - Plays random `.mp3` files from a designated music folder using the `pygame` library.

6. **Camera Functionality**:
   - Captures images from the webcam using the `cv2` (OpenCV) library.
   - Includes a countdown timer before taking a photo.

7. **Folder Management**:
   - Opens specific folders on the system, ensuring the folder exists before attempting to access it.

8. **Graceful Exit**:
   - Listens for `exit` or `stop` commands to terminate the program.
   - Handles interruptions (e.g., `KeyboardInterrupt`) gracefully.

## Libraries Used
1. **pyttsx3**:
   - For text-to-speech functionality.
2. **speech_recognition**:
   - For voice input and command recognition.
3. **os**:
   - For file and folder operations.
4. **datetime**:
   - To fetch the current time.
5. **webbrowser**:
   - To open websites in the default browser.
6. **pygame**:
   - For music playback.
7. **cv2 (OpenCV)**:
   - For webcam access and image capture.
8. **time**:
   - For timer functionality in the camera module.
9. **random**:
   - To select a random music file.

## How It Works
1. The assistant starts by greeting the user.
2. It listens for voice commands using a microphone.
3. Depending on the command, it performs one of the following tasks:
   - Opens a predefined website.
   - Announces the current time.
   - Plays music from the specified folder.
   - Opens the webcam and captures an image after a countdown.
   - Opens a specific folder on the system.
4. The program continues to listen for commands in a loop until the user says "exit" or "stop."

## Commands Examples
- **Open websites**: "Open Google," "Open YouTube."
- **Get the time**: "What is the time?"
- **Play music**: "Play music."
- **Capture photo**: "Open camera."
- **Open folder**: "Open folder web development."
- **Exit program**: "Exit," "Stop."

## Future Enhancements
- Add more complex natural language processing for better understanding of user queries.
- Enable integration with external APIs for weather updates, news, and more.
- Add task scheduling and reminders.
- Implement a GUI for better user interaction.


