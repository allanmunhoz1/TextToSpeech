# ##############################################
#           Text To Speech  --  Python
# ##############################################

# pip install pyttsx3
import pyttsx3

engine = pyttsx3.init()

engine.say("Hi, This is  Allan Munhoz")
engine.say("Good afternoon")
engine.say("See example")
engine.say("Text To Speech")
engine.say("Thank you")
engine.runAndWait()