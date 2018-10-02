# ask the user where to look 
print("Where should I look?")
place = input()

# work out if the battery is there
if (place == "in the bedroom"):
  print("Where in the bedroom should I look?")
  place = input() 

  if (place == "under the bed"):
    print("Found some shoes but no battery.")
  else: 
    print("There is mess but no battery.")
else:
  print("I don't know where that is but I will keep looking.")
