# 1) If the user's entry is longer than 5 characters, print "Your entry is longer than 5 characters!" Otherwise, print nothing.
user_entry = input('Enter a word: ')
if len(user_entry) > 5:
    print("Your entry is longer than 5 characters!")


# 2) If the number entered by the user is 100 or larger, print "Valid entry!"  Otherwise, print, "Number too small."
num_entry = int(input('Enter a number larger than 100: '))
if num_entry > 100:
    print("Valid entry!")
else:
    print("Number too small.")



# 3) Prompt the user to enter a lowercase letter. Use the 'in' operator to check if the letter is a vowel (e.g. in the string 'aeiou'). If so, print, "___ is a vowel." Else, print, "___ is NOT a vowel."
# 4) What happens if the user enters a capital letter instead of lowercase? Refactor your code for problem 3 so that it works for both capital and lowercase vowels!
user_letter = input('Enter a letter: ')
vowels = 'aeiou'
if user_letter.lower() in vowels:
    print(user_letter, "is a vowel.")
else:
    print(user_letter, "is NOT a vowel.")

