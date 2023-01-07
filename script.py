"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("The challenge has begun")

name = input("Enter a name: ")
print(name)

adjective1 = input("Guess the first adjective in the story: ")

adjective2 = input("Guess the second adjective in the story: ")

adjective3 = input("Guess the third adjective in the story: ")

verb = input("Guess the verb in the story: ")

noun1 = input("Guess the first noun in the story: ")

noun2 = input("Guess the second noun in the story: ")

animal = input("Guess the animal used in the story: ")

food = input("Guess the food used in the story: ")

fruit = input("Guess the fruit used in the story: ")

superhero = input("Guess the superhero used in the story: ")

country = input("Guess the country used in the story: ")

dessert = input("Guess the dessert used in the story: ")

year = input("Guess the year used in the story: ")

print("Well done! Here's your result: ")
print(STORY % (name, adjective1, adjective2, animal, food, verb, noun1, fruit, adjective3, name, superhero, name, country, name, dessert, name,  year, noun2))






















