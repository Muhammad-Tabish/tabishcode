input_string = input("Enter a String: ")
input_string = input_string.casefold()

vowels = "aeiou"

vowels_data = {}.fromkeys(vowels, 0)

print(vowels_data)

for characters in input_string:
    print(characters)


