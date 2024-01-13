import re
import random
import time

def pause():
    print("Awaiting...")

def border():
    print("====="*25)

botName = "ChatBot: "

greating = ["Hi", "Hello"]
farewell = ["Bye", "Goodbye"]

while True:
    border()
    x = input("You\t: ")
    if re.findall(r'hi|hello', x):
        border()
        pause()
        time.sleep(1)
        print(botName + random.choice(greating))
    elif re.findall(r'bye|goodbye', x):
        border()
        pause()
        time.sleep(1)
        print(botName + random.choice(farewell))