
sentence = input("Enter a sentence: ")

vowels_list = "aeiouAEIOU"
words = 0
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for char in sentence:
    if char.isalpha():
        if char in vowels_list:
            vowels += 1
        else:
            consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
    else:
        special += 1

words = len(sentence.split())

total_letters = vowels + consonants

vowel_percentage = (vowels / total_letters) * 100 if total_letters > 0 else 0.0

print("===============================================")
print("DOCUMENT ANALYSIS REPORT")
print("===============================================")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}\n")

print("--- Character Breakdown ---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special}\n")

print("--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print("===============================================")
print("Analysis Complete!")
print("===============================================")