# Ask user to enter 3 numbers
print("Please enter first number")
first_number = int(input())

print("Please enter second number")
second_number = int(input())

print("Please enter third number")
third_number = int(input())

# Work out how many are even and how many are odd
even_count = 0
odd_count = 0

if (first_number & 2 == 0):
  even_count = even_count + 1
  # or even_count += 1
else:
  odd_count = odd_count + 1

if (second_number & 2 == 0):
  even_count = even_count + 1
  # or even_count += 1
else:
  odd_count = odd_count + 1

if (third_number & 2 == 0):
  even_count = even_count + 1
  # or even_count += 1
else:
  odd_count = odd_count + 1

print("Total even numbers:", even_count)
print("Total odd numbers", odd_count)
