#import re

palavra1 = input('Primeira palavra: ')
palavra2 = input('Segunda palavra: ')
palavra3 = input('Terceira palavra: ')

palavra1 = palavra1.upper()
palavra2 = palavra2.lower()

#palavra3 = re.sub("[aeiouAEIOU]", "", palavra3)

disallowed_characters = "aeiouAEIOU"

for character in disallowed_characters:
    palavra3 = palavra3.replace(character, "")

print(palavra1)
print(palavra2)
print(palavra3.upper())