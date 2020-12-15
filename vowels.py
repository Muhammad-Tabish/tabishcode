input_string = input("Enter a String: ")
input_string = input_string.casefold()

vowels = "aeiou"

vowels_data = {}.fromkeys(vowels, 0)
total_vowels = 0

print(vowels_data)

for characters in input_string:
    print(characters)
    if characters in vowels:
        vowels_data[characters] += 1
        total_vowels +=1
print("total vowels count: ", total_vowels)
for vowel in vowels_data:
    print(vowel, " =>", vowels_data[vowel])


