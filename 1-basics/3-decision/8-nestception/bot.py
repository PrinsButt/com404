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
    
elif (place == "in the bathroom"):
  print("Where in the bathroom should I look?")
  place = input() 

  if (place == "in the bathtub"):
    print("Found a duck but no battery.")
  else: 
    print("It is wet but there is no battery.")

elif (place == "in the lab"):
    print("Where in the lab should I look?")
    place = input() 

    if (place == "on the table"):
      print("Found the battery. Hurray!")
    else: 
      print("There are lots of tools but no battery.")
else:
  print("I am not sure where that is but I will keep looking")
