#input function helps to get the input from the user
value = input("Enter a word: ")
output = value[::-1]
#Checking length will help if user press Enter without entering any input
if len(value) == 0:
    print("No word has been entered")
elif value == output:
    print("The given word is palindrome")
else:
    print("The given word is not palindrome")

