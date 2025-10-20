personName = input("Enter a person name: ") # Tig
noun1 = input("Enter a noun: ") # matches 
adjective1 = input("Enter an adjective: ") # excited
verb1 = input("enter a verb: ") #sleep
adjective2 = input("Enter an adjective2: ") # scary
animal1 = input("Enter an animal: ") # bear
verb2 = input("Enter a verb: ") # swim
colorLake = input("Enter a color; ") # blue
verb_ing = input("Enter a verb ending in ing: ") # swimming
adverb = input("Enter an adverb ending in ly: ") # bravely
nomber_of_time = input("Enter number of time: ") # 7 long hours
colorAnimal = input("Enter color of animal: ") #broun
animal2 = input("Enter an animal: ") # squirell
nomber_of_stories = input("Enter a number: ") # 100 silly stories
noun2 = input("Enter a noun: ") # potatoes

myorder = """ This weekend I am going camping with {}. I packed my lantern, sleeping bag, and {}. 
I am so {} to {} in a tent. I am {} we might see a {}, I hear they’re kind of dangerous. While we’re 
camping, we are going to hike, fish, and {}. I have heard that the {} lake is great for {}. Then we will 
{} hike through the forest for {}. If I see a {} {} while hiking, I am going to bring it home as 
 a pet!At night we will tell {} stories and roast {} around the campfire!! """

print(myorder.format(personName, noun1, adjective1, verb1, adjective2, animal1, verb2, colorLake, verb_ing, adverb, nomber_of_time, colorAnimal, animal2, nomber_of_stories, noun2))
