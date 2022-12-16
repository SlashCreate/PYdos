print("PYdos BETA")
print("Type 'help' for commands\n")

cmdIn = 0
args = 0
cmd = 0
a = 0

def cmdRun():
  cmdIn = input("pydos>")
  args = cmdIn.split("#")
  cmd = args[0]

  if cmd == "print":
     print(args[1])
     print(" ")
     cmdRun()

  if cmd == "help":
     print("\nprint#<text>\nclear\nhelp\ngit ")
     print("")
     cmdRun() 

  if cmd == "clear":
     import os
     os.system('clear')
     cmdRun()

  if cmd == "git":
     print("github: https://github.com/SlashCreate/PYdos")
     print(" ")
     cmdRun()
  cmdRun()

cmdRun()
