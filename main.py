import os
import time
global welcome


def introSeq():
  wait = time.sleep(0.5)
  print("While waiting for your iPad to be updated,")
  wait
  print("The walls shift, and you see a secret passageway.")
  wait
  print("You enter.")

def menuScreen():
  t = open("menu.txt", "r")
  print(t.read())
  time.sleep(2)
  start = input("Press enter to start. ")

  if start == "":
    welcome = True

introSeq()
menuScreen()

if welcome == True:
  t = open("welcomeToHell.txt", "r")
  print(t.read())

