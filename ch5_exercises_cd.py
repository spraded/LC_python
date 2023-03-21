# 1) The following code should determine if a number is divisible by 2, 3, both, or neither, but as written it does not behave as we want. Rearrange the order of the if, elif, and else code blocks as needed to give the desired results.

num = 7 # Try the values 10, 15, and 7 as well.

if num%2 == 0 and num%3 == 0:
  print(num, "is divisible by 2 and 3.")
elif num%2 == 0:
  print(num, "is divisible by 2.")
elif num%3 == 0:
  print(num, "is divisible by 3.")
else:
  print(num, "is NOT divisible by 2 or 3.")

# 2) Given the score on an exam, use a chained conditional to assign it the proper letter grade. Assume a standard 10-point scale (A = 100 - 90, B = 89 - 80, C = 79 - 70, etc.). Print the results as ___% = ___. Fill in the first blank with the score and the second blank with the letter grade.
score = float(input('Enter a score: '))

if score>100:
    print("Invalid score. Enter a number between 0-100")
elif score>=90:
  print(score,"% = A")
elif score>=80:
  print(score,"% = B")
elif score>=70:
  print(score,"% = C")
elif score>=60:
  print(score,"% = D")
else:
  print(score, "% = F")



# 3) Pick an activity based on the current weather. If the weather is hot and rainy, your code should tell you to watch Netflix. For hot and dry conditions, it should tell you to go swimming. If cold and rainy, it should tell you to get under a blanket and read. If it is cold and dry, it should tell you to go meet a friend.
temperature = 'cold'
humidity = 'dry'

if temperature == 'hot' and humidity == 'rainy':
  print('Watch netflix.')
elif temperature == 'hot' and humidity == 'dry':
  print('Go swimming.')
elif temperature == 'cold' and humidity == 'rainy':
  print('Get under a blanket and read.')
elif temperature == 'cold' and humidity == 'dry':
  print('Go meet a friend.')

# 4) Nested conditionals: If the customer chooses a salad, ask them for a dressing option (ranch or italian). If they choose burger ask them if they want cheese (yes or no). Print out their final order.
lunch_selection = input('Welcome! Would you like a burger or a salad? ')
drink_selection = input('What would you like to drink? ')
cost = 0

if drink_selection.lower() != 'water':
   cost += 3
if lunch_selection.lower() == "salad":
  dressing_selection = input('Would you like ranch or italian dressing? ')
  cost += 13
  if dressing_selection.lower() == "ranch" or dressing_selection == "italian":
    print("You ordered a", lunch_selection, "with", dressing_selection, "dressing and", drink_selection + ". Your total is $" + str(cost) + ".")
else:
    if lunch_selection.lower() == "burger":
        cheese_selection = input("Would you like cheese? ")
        cost += 15
        if cheese_selection.lower() == 'yes':
            cost += 2
            print("You ordered a", lunch_selection, "with cheese and", drink_selection + ". Your total is $" + str(cost) + ".")
        else:
            print("You ordered a", lunch_selection, "without cheese and", drink_selection + ". Your total is $" + str(cost) + ".")
      



# 5) Each food option has a different price. Add a cost variable to your lunch code and calculate the bill for the lunch order. Include this in the print statement.