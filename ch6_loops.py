import turtle

#For loop scratches
for num in range(0, 21, 5):
    print(num)
    print("Hello" * num)

for number in range(10):
   print("I have", 12 - number, "cookies. I'm going to eat one!")

#For loop range 
    # Print the numbers 0 - 5.
for num in range(1, 6):
    print(num)

    # Print the numbers 33 - 45, including 45.
for num in range(33, 46):
    print(num)

    # Print only the odd numbers from 0 - 20.
for num in range(1, 20, 2):
    print(num)

    # Print the numbers 25, 35, 45…95.
for num in range(25, 96, 10):
    print(num)

    # Print the numbers from -3 to -10.
for num in range(-3, -11, -1):
    print(num)

    # Print by 3’s from 15 to -21.
for num in range(15, -22, -3):
    print(num)

#Range with variables
start_value = int(input("Enter the FIRST number to print: "))
end_value = int(input("Enter the LAST number to print: "))
step_value = int(input("Enter the step value for the loop: "))

for num in range(start_value, end_value+1, step_value):
    print(num)

#For loop turtle square
window = turtle.Screen()
pet = turtle.Turtle()
num_sides = 9
turn_angle = 360.0 / num_sides

for side in range(num_sides):
    pet.forward(50)
    pet.left(turn_angle)

window.exitonclick()

#Accumulator with strings
only_vowels = ''
vowels = 'aeiou'
some_text = 'We are coding a program about vowels.'

for character in some_text:
    if character.lower() in vowels:
        only_vowels += character

print("The sentence:", some_text, "includes these vowels:", only_vowels)
