import random

def get_nonempty_input(prompt):
    """Prompt user until they enter a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be blank. Please try again.")

def get_numeric_input(prompt):
    """Prompt user until they enter a valid number."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return value
        print("Please enter a valid number.")

choice = input("Enter the number of the template you want to use (1-3): ").strip()

if choice == "1":
    number = get_numeric_input("Type a number: ")
    measure_time = get_nonempty_input("Type a measure of time: ")
    transport = get_nonempty_input("Type a mode of transportation: ")
    adj1 = get_nonempty_input("Type an adjective: ")
    adj2 = get_nonempty_input("Type another adjective: ")
    noun = get_nonempty_input("Type a noun: ")
    color = get_nonempty_input("Type a color: ")
    body_part = get_nonempty_input("Type a part of the body: ")
    verb = get_nonempty_input("Type a verb: ")
    number2 = get_numeric_input("Type another number: ")
    noun2 = get_nonempty_input("Type another noun: ")
    noun3 = get_nonempty_input("Type another noun: ")
    body_part2 = get_nonempty_input("Type another part of the body: ")
    verb2 = get_nonempty_input("Type another verb: ")
    noun4 = get_nonempty_input("Type another noun: ")
    adj3 = get_nonempty_input("Type another adjective: ")
    silly = get_nonempty_input("Type a silly word: ")

    story = (
        f"It was about {number} {measure_time} ago when I arrived at the hospital in a {transport}. "
        f"The hospital is a/an {adj1} place, there are a lot of {adj2} {noun} here. "
        f"There are nurses here who have {color} {body_part}. "
        f"If someone wants to come into my room I told them that they have to {verb} first. "
        f"I’ve decorated my room with {number2} {noun2}. "
        f"Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. "
        f"I heard that all doctors {verb2} {noun4} every day for breakfast. "
        f"The most {adj3} thing about being in the hospital is the {silly} {noun}!"
    )

elif choice == "2":
    name = get_nonempty_input("Type a person’s name: ")
    noun = get_nonempty_input("Type a noun: ")
    adj1 = get_nonempty_input("Type a feeling adjective: ")
    verb = get_nonempty_input("Type a verb: ")
    adj2 = get_nonempty_input("Type another feeling adjective: ")
    animal = get_nonempty_input("Type an animal: ")
    verb2 = get_nonempty_input("Type another verb: ")
    color = get_nonempty_input("Type a color: ")
    verb_ing = get_nonempty_input("Type a verb ending in 'ing': ")
    adverb = get_nonempty_input("Type an adverb ending in 'ly': ")
    number = get_numeric_input("Type a number: ")
    measure_time = get_nonempty_input("Type a measure of time: ")
    color2 = get_nonempty_input("Type another color: ")
    animal2 = get_nonempty_input("Type another animal: ")
    silly = get_nonempty_input("Type a silly word: ")
    noun2 = get_nonempty_input("Type another noun: ")

    story = (
        f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. "
        f"I am so {adj1} to {verb} in a tent. I am {adj2} we might see a(n) {animal}, "
        f"I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. "
        f"I have heard that the {color} lake is great for {verb_ing}. "
        f"Then we will {adverb} hike through the forest for {number} {measure_time}. "
        f"If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet! "
        f"At night we will tell {number} {silly} stories and roast {noun2} around the campfire!"
    )

elif choice == "3":
    name = get_nonempty_input("Type a person’s name: ")
    adj1 = get_nonempty_input("Type an adjective: ")
    color = get_nonempty_input("Type a color: ")
    animal = get_nonempty_input("Type an animal: ")
    place = get_nonempty_input("Type a place: ")
    adj2 = get_nonempty_input("Type another adjective: ")
    creature1 = get_nonempty_input("Type a magical creature (plural): ")
    adj3 = get_nonempty_input("Type another adjective: ")
    creature2 = get_nonempty_input("Type another magical creature (plural): ")
    room = get_nonempty_input("Type a room in a house: ")
    noun = get_nonempty_input("Type a noun: ")
    noun2 = get_nonempty_input("Type another noun: ")
    noun3 = get_nonempty_input("Type a plural noun: ")
    adj4 = get_nonempty_input("Type another adjective: ")
    noun4 = get_nonempty_input("Type another plural noun: ")
    number = get_numeric_input("Type a number: ")
    measure_time = get_nonempty_input("Type a measure of time: ")
    verb_ing = get_nonempty_input("Type a verb ending in 'ing': ")
    adj5 = get_nonempty_input("Type another adjective: ")
    noun5 = get_nonempty_input("Type another noun: ")

    story = (
        f"Dear {name}, I am writing to you from a {adj1} castle in an enchanted forest. "
        f"I found myself here one day after going for a ride on a {color} {animal} in {place}. "
        f"There are {adj2} {creature1} and {adj3} {creature2} here! "
        f"In the {room} there is a pool full of {noun}. "
        f"I fall asleep each night on a {noun2} of {noun3} and dream of {adj4} {noun4}. "
        f"It feels as though I have lived here for {number} {measure_time}. "
        f"I hope one day you can visit, although the only way to get here now is "
        f"{verb_ing} on a {adj5} {noun5}!"
    )

else:
    story = "Invalid choice. Please restart and pick 1, 2, or 3."

print("\n" + story)
