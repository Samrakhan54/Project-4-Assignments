# Mad Libs Game

print("Welcome to the Mad Libs game!")

# Taking inputs from user
adj = input("Type an adjective: ")
animal = input("Type an animal: ")
action = input("Type a verb: ")
reaction = input("Type something you would shout: ")

# Creating the story
print("\nHere's your funny story:")
print("Today, I went to the zoo and saw a", adj, animal + ".")
print("It suddenly", action, "and everyone got scared.")
print("I yelled:", reaction + "!")
