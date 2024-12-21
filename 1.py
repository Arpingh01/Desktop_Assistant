import pyttsx3
import speech_recognition as sr
import os
import datetime
import webbrowser
import pygame
import random
import cv2
import time


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        try:
            print("Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Listening timeout occurred.")
            return ""
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except Exception as e:
            print(f"Error: {str(e)}")
            return ""


if __name__ == '__main__':
    print('PyCharm')
    say("Hello Arpita, I am your Personal AI")
    try:
        while True:
            query = takeCommand()

            if not query:
                continue

            # Open websites
            sites = [["google", "https://www.google.com"], ["youtube", "https://www.youtube.com"],
                     ["facebook", "https://www.facebook.com"], ["instagram", "https://www.instagram.com"],
                     ["whatsapp", "https://www.whatsapp.com"], ["yahoo", "https://www.yahoo.com"],
                     ["reddit", "https://www.reddit.com"], ["amazon", "https://www.amazon.com"],
                     ["myntra", "https://www.myntra.com"], ["netflix", "https://www.netflix.com"],
                     ["linkedin", "https://www.linkedin.com"], ["quora", "https://www.quora.com"],
                     ["pinterest", "https://www.pinterest.com"], ["canva", "https://www.canva.com"],
                     ["spotify", "https://www.spotify.com"], ["wikipedia", "https://www.wikipedia.com"],
                    ["twitter", "https://www.twitter.com"],]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say(f"OK Arpita, Opening {site[0]}")
                    webbrowser.open(site[1])

            # Time
            if "what is the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Arpita, the time is {strfTime}")

            # Play music
            elif 'play music' in query:
                pygame.mixer.init()
                folder = r'C:\Users\DELL\PycharmProjects\Desktop_Assistant\Sample_music'
                files = [file for file in os.listdir(folder) if file.endswith('.mp3')]
                if files:
                    random_mp3 = random.choice(files)
                    file_path = os.path.join(folder, random_mp3)
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    say(f"Playing {random_mp3}")
                else:
                    say("No music files found.")
            elif 'open camera' in query:
                TIMER = int(5)
                cap = cv2.VideoCapture(0)

                while True:
                    ret, img = cap.read()
                    cv2.imshow('arpita', img)
                    k = cv2.waitKey(5)
                    if k == ord('c'):
                        prev = time.time()

                        while TIMER >= 0:
                            ret, img = cap.read()

                            font = cv2.FONT_HERSHEY_SIMPLEX
                            cv2.putText(img, str(TIMER),
                                        (200, 250), font,
                                        7, (0, 255, 255),
                                        4, cv2.LINE_AA)
                            cv2.imshow('picture', img)
                            cv2.waitKey(5)
                            cur = time.time()

                            if cur - prev >= 1:
                                prev = cur
                                TIMER = TIMER - 1

                        else:
                            ret, img = cap.read()

                            cv2.imshow('a', img)

                            cv2.waitKey(5)

                            cv2.imwrite('camera.jpg', img)

                    elif k == 27:
                        break

                cap.release()

                cv2.destroyAllWindows()


            # Open folder
            elif 'open folder web development' in query:
                folder_path = r"C:\Users\DELL\OneDrive\Desktop\WebDevelop"
                if os.path.exists(folder_path):
                    os.startfile(folder_path)
                else:
                    say("The specified folder does not exist.")

            # Exit
            elif "exit" in query or "stop" in query:
                say("Goodbye Arpita!")
                break
    except KeyboardInterrupt:
        say("Goodbye Arpita")
