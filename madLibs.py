import random

print("Choose a template: 1, 2, or 3")
choice = input("Enter your choice: ")

if choice.isdigit() and int(choice) in (1, 2, 3):
    choice = int(choice)
else:
    choice = random.randint(1, 3)
    print(f"Invalid choice. Random template selected: {choice}")

print()

# ---------- TEMPLATE 1 ----------
if choice == 1:
    num = input("Enter a number: ")
    time = input("Enter a measure of time: ")
    transport = input("Enter a mode of transportation: ")
    adj1 = input("Enter an adjective: ")
    adj2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    color = input("Enter a color: ")
    body1 = input("Enter a part of the body: ")
    verb1 = input("Enter a verb: ")
    num2 = input("Enter another number: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    body2 = input("Enter another part of the body: ")
    verb2 = input("Enter a verb: ")
    noun4 = input("Enter another noun: ")
    adj3 = input("Enter another adjective: ")
    silly = input("Enter a silly word: ")
    noun5 = input("Enter one last noun: ")

    print("\n--- Template 1, Your Story ---\n")
    print(f"""
It was about {num} {time} ago when I arrived at the hospital in a {transport}.
The hospital is a {adj1} place, there are a lot of {adj2} {noun1} here.
There are nurses here who have {color} {body1}.
If someone wants to come into my room I told them that they have to {verb1} first.
I’ve decorated my room with {num2} {noun2}.
Today I talked to a doctor and they were wearing a {noun3} on their {body2}.
I heard that all doctors {verb2} {noun4} every day for breakfast.
The most {adj3} thing about being in the hospital is the {silly} {noun5}!
""")

# ---------- TEMPLATE 2 ----------
elif choice == 2:
    name = input("Enter a person's name: ")
    noun1 = input("Enter a noun: ")
    adj1 = input("Enter a feeling adjective: ")
    verb1 = input("Enter a verb: ")
    adj2 = input("Enter another feeling adjective: ")
    animal = input("Enter an animal: ")
    verb2 = input("Enter another verb: ")
    color = input("Enter a color: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adverb = input("Enter an adverb ending in -ly: ")
    num = input("Enter a number: ")
    time = input("Enter a measure of time: ")
    color2 = input("Enter another color: ")
    animal2 = input("Enter another animal: ")
    num2 = input("Enter another number: ")
    silly = input("Enter a silly word: ")
    noun2 = input("Enter another noun: ")

    print("\n--- Template 2, Your Story ---\n")
    print(f"""
This weekend I am going camping with {name}.
I packed my lantern, sleeping bag, and {noun1}.
I am so {adj1} to {verb1} in a tent.
I am {adj2} we might see a(n) {animal}, I hear they’re kind of dangerous.
While we’re camping, we are going to hike, fish, and {verb2}.
I have heard that the {color} lake is great for {verb_ing}.
Then we will {adverb} hike through the forest for {num} {time}.
If I see a {color2} {animal2} while hiking, I am going to bring it home as a pet!
At night we will tell {num2} {silly} stories and roast {noun2} around the campfire!!
""")

# ---------- TEMPLATE 3 ----------
else:
    name = input("Enter a person's name: ")
    adj1 = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adj2 = input("Enter another adjective: ")
    creature1 = input("Enter a magical creature (plural): ")
    adj3 = input("Enter another adjective: ")
    creature2 = input("Enter another magical creature (plural): ")
    room = input("Enter a room in a house: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter a plural noun: ")
    adj4 = input("Enter another adjective: ")
    noun4 = input("Enter another plural noun: ")
    num = input("Enter a number: ")
    time = input("Enter a measure of time: ")
    verb_ing = input("Enter a verb ending in -ing: ")
    adj5 = input("Enter another adjective: ")
    noun5 = input("Enter another noun: ")

    print("\n--- Template 3, Your Story ---\n")
    print(f"""
Dear {name},
I am writing to you from a {adj1} castle in an enchanted forest.
I found myself here one day after going for a ride on a {color} {animal} in {place}.
There are {adj2} {creature1} and {adj3} {creature2} here!
In the {room} there is a pool full of {noun1}.
I fall asleep each night on a {noun2} of {noun3} and dream of {adj4} {noun4}.
It feels as though I have lived here for {num} {time}.
I hope one day you can visit, although the only way to get here now is
{verb_ing} on a {adj5} {noun5}!
""")