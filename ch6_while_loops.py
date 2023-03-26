#Convert for to while loop
letters = 'abcdefghijklmnopqrstuvwxyz'
for_string = ''
num_letters = 8


for index in range(num_letters):
   for_string += letters[index]

print(for_string)

index = 0
while_string = ''
while index < num_letters:
   while_string += letters[index]
   index += 1

print(while_string)
print(letters)

#While input validation
num_choice = 0

while num_choice <= 0:
  num_choice = int(input('Choose a positive number: '))
  if num_choice <= 0:
    print('Invalid number')
