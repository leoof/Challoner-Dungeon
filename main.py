## Importing modules for later use in the program
import os
import random
import time

## Command(s)
def txtSplit():
  global inputlist
  global length
  unsplitted = cmdInput
  inputlist = unsplitted.split(' ')
  length = len(inputlist)
  print(inputlist)
  print(length)

## Add more ideas for trap rooms, easy, medium or hard
## Will also be adding corridors and stuff where you can get rushed by enemies with a danger level based on the room
trapRooms = {
  "platetrap" : "easy", #pressure plate triggers a dart trap or boulder or smth idk llo
  
}



def menuScreen():
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

def roomReader(room):
  global currentRoom
  currentRoom = random.choice(rooms) 
  if currentRoom == "platetrap":
    roomPlateTrap()

menuScreen()

roomReader()