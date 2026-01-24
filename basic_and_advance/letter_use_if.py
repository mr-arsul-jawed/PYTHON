letter  = input("Enter a letter: ")

if (letter in 'aeiouAEIOU'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")



letter = input("enter the letter: ")

if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is vowel")
else: 
    print("it is not vowel")