# For loop exercises

# Numbers
    # Print the numbers 0 - 20, one number per line.
for num in range(0, 21):
    print(num)

    # Print only the ODD values from 3 - 29, one number per line.
for num in range(3, 30, 2):
    print(num)

    # Print the EVEN numbers 12 down to -14 in descending order, one number per line.
for num in range(12, -15, -2):
    print(num)

    # Print the numbers 50 down to 20 in descending order, but only if the numbers are multiples of 3.
for num in range(50, 21, -1):
    if num % 3 == 0:
        print(num)

# String - LaunchCode
string = 'LaunchCode'
    # Print out each character of the string, one letter per line. Do this WITHOUT using index values.
for char in string:
    print(char)

    # Now use index values to print each character of the string—in reverse order—to a new line. Recall that you can access a single character from a string with the syntax var_name[index], where index is an integer value, and var_name is the variable used to store the string.
max_index = len(string)-1

for index in range(max_index, -1, -1):
    print(string[index])

#String - gibberish
    # print every fifth character, including the first character. Use index values and range(start, stop, step).
gibberish = 'Vna#hewzB*rQhT%yq^lv %iPwgOexWo &C^oUoGSdtJLj'

for index in range(0, len(gibberish), 5):
    print(gibberish[index])

#Bonus - reformat with modulus and conditional
for index in range(len(gibberish)):
    if index % 5 == 0:
        print(gibberish[index])


# While loop exercises