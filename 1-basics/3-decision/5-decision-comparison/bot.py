# Read in user's first number
print("Please enter first number")
first_number = float( input() )

# Read in user's second number 
print("Please enter second number")
second_number = float( input() )

# Work out which number is bigger
if (second_number > first_number):
  print("Second number is greater.")
elif (first_number > second_number):
  print("First number is greater.")
else:
  print("The numbers are equal.")
