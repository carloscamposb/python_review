from data import all_list
from art import logo_ranking, themes
import random

theme_number = 0 
text_theme = ''
new_list = []

# FUNCTIONS
def phrase_estructure(data, theme_number):
    if theme_number == 1:
         return f"The {data['breed']} is the dog I like the most."
    elif theme_number == 2:
        return f"{data['feeling']} frequently."
    elif theme_number == 3:
        return f"The {data['name']} scares me a lot."
    elif theme_number == 4:
        return f"{data['name']} is a country that I would like to visit someday"
    elif theme_number == 5:
        return f"The {data['name']} scares me a lot."
    elif theme_number == 6:
        return f"{data['name']} is one of the best cartoons I’ve ever seen."
    elif theme_number == 7:
        return f"{data['name']} is one of the best things I’ve ever seen."
    else:
        return f"{data['name']} is the color I like the most."

def add_phrases():
    return [phrase_estructure(item, theme_number) for item in random_theme]

def inside_list(question, phrase):
    if len(new_list[question - 1]['number']) > 2:
        print("⚠️ This field is already complete")
    else:
        new_list[question - 1]['number'] += " " + phrase

# START
print(logo_ranking)
print('Welcome and enjoy')

while theme_number not in range(1, 9):
    theme_number = int(input('Choose a theme:\n(1)Dogs 🐕\n(2)Feelings 😃🥲\n(3)Insects 🦋\n(4)Country 🏳️\n(5)Monsters 🩻\n(6)Cartoons 📺\n(7)Movies and Series 📽️\n(8)Colors🎨\nYour choice: '))
    if theme_number not in range(1, 9):
        print('Please, repeat using a valid number')

new_theme = all_list[theme_number - 1]
text_theme = themes[theme_number - 1]
random_theme = random.sample(new_theme, k=5)

new_list = [{'number': f'{i+1}-'} for i in range(5)]

print("\n" * 5)
print(f"{text_theme} — Rank from 1 to 5 what impacts you the most:")

phrases = add_phrases()

for i, phrase in enumerate(phrases):
    print(f"\n{i+1}. {phrase}")
    while True:
        try:
            question = int(input("Rank (1 to 5): "))
            if question in range(1, 6):
                inside_list(question, phrase)
                break
            else:
                print("⚠️ Please, use a number from 1 to 5.")
        except ValueError:
            print("⚠️ Please, enter a valid number.")

print("\n✅ Final ranking:")
for item in new_list:
    print(item['number'])
