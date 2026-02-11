def main():

    user_input = input("Favorite Fruit: ").lower()
    for fruit in fruits:
        if user_input == fruit["name"]:
            print("Calories: ", fruit["calories"])

fruits = [
    {"name": "apple", "calories": "130"},
    {"name": "avocado", "calories": "50"},
    {"name": "banana", "calories": "110"},
    {"name": "cantaloupe", "calories": "50"},
    {"name": "grapefruit", "calories": "60"},
    {"name": "grapes", "calories": "90"},
    {"name": "honeydew melon", "calories": "50"},
    {"name": "kiwifruit", "calories": "90"},
    {"name": "lemon", "calories": "15"},
    {"name": "lime", "calories": "20"},
    {"name": "nectarine", "calories": "60"},
    {"name": "orange", "calories": "80"},
    {"name": "peach", "calories": "60"},
    {"name": "pear", "calories": "100"},
    {"name": "pineapple", "calories": "50"},
    {"name": "plums", "calories": "70"},
    {"name": "strawberries", "calories": "50"},
    {"name": "sweet cherries", "calories": "100"},
    {"name": "tangerine", "calories": "50"},
    {"name": "watermelon", "calories": "80"},
]

main()


'''
implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text.
Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.


'''
