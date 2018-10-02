# Read direction from user 
print("Please enter one of the following:")
print("...w to move up")
print("...s to move down")
print("...a to move left")
print("...d to move right")

direction = input()

if (direction == "w"):
  print("I will move up.")
elif (direction == "s"):
  print("I will move down.")
elif (direction == "a"):
  print("I will move left.")
elif (direction == "d"):
  print("I will move right.")
else:
  print("Error! Please specify again.")
