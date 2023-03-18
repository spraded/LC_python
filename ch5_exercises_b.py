# 1) Given an integer, check to see if the number is even and divisible by 5. Print an appropriate message depending on the result.
user_entry = int(input("Enter a whole number: "))

if user_entry % 5 == 0:
  print("Your number is divisible by 5.")
else:
  print("Your number is not divisible by 5.")


# 2) Given a string, print, "___ is a really long word!" if the string is longer than 9 characters and does NOT contain a space. Otherwise, print, "___ is either short, or it contains multiple words." Fill in the blank with the original string.
test_string_1 = 'bookkeepers'
test_string_2 = 'Apricots and apples'
test_string_3 = 'carrot'
test_string_4 = 'apple pie'

if len(test_string_1) > 9 and " " not in test_string_1:
  print(test_string_1, "is a really long word!")
else:
  print(test_string_1, "is either too short or contains multiple words.")

if len(test_string_2) > 9 and " " not in test_string_2:
  print(test_string_2, "is a really long word!")
else:
  print(test_string_2, "is either too short or contains multiple words.")

if len(test_string_3) > 9 and " " not in test_string_3:
  print(test_string_3, "is a really long word!")
else:
  print(test_string_3, "is either too short or contains multiple words.")

if len(test_string_4) > 9 and " " not in test_string_4:
  print(test_string_4, "is a really long word!")
else:
  print(test_string_4, "is either too short or contains multiple words.")


# 3) Refactor the following code to check if 'letter' is NOT in the string 'BCDFGHJKLMNPQRSTVWXYZ' or is a lowercase vowel. How does making this change affect the if/else code blocks?
letter = 'A'
cap_consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
vowels = 'aeiou'

if letter not in cap_consonants or letter in vowels:
  print("'" + letter + "'", "is either a lowercase vowel OR a lowercase consonant.")
else:
  print("Pick a capital consonant or a lowercase vowel")

# 4) Indicate whether each of following expressions returns True or False.
num = 5

print(num >= 0 and num*2 <= 50 and num%2 == 0)
print(num >= 0 or num*2 <= 50 or num%2 == 0)
print(num >= 0 and num*2 <= 50 or num%2 == 0)
print(num >= 0 or num*2 <= 50 and num%2 == 0)
print(not num < 0 and num%3 != 0)
print(not (num%3 == 0 or num*4 >= 20))