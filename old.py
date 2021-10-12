import os
import random
import time

rooms = ["platetrap"]

def introSeq():
  time.sleep(1)
  print("WHILE WAITING FOR YOUR IPAD TO BE UPDATED,")
  time.sleep(1)
  print("THE WALLS SHIFT, REVEALING A SECRET PASSAGEWAY")
  time.sleep(1)
  print("YOU DECIDE TO TAKE A DETOUR TO YOUR NEXT LESSON.")

def menuScreen():
  time.sleep(1)
  t = open("menu.txt", "r")
  print(" ")
  print(t.read())


def roomPlateTrap():
  print("there is pressure plate lol. If you dont jump you die")
  try:
    choice = str(input("What will you do?")).lower
    if choice == "run":
      print("You died lol")
  except:
    print("Nah")

def roomReader():
  global currentRoom
  currentRoom = random.choice(rooms)
  if currentRoom == "platetrap":
    roomPlateTrap()

introSeq()
menuScreen()

roomReader()