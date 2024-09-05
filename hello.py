name = input("What's your name? ") 
greeting = "Hello "
print(greeting + name)

feeling = input("How are you feeeling today? ")
if feeling == "sad":
    print("Feel better so then!")
elif feeling == "Sad":
    print("Feel better so then!")
elif feeling == "happy":
    print("That's great" + name + "!")
elif feeling == "Happy":
    print("That's great" + name + "!")
else:
    print("That's good") 
    
color = input("What's your favorite color? ") 
print(color + " is an great color")

book = input("What's your favorite book? ")
if book == ("I don't have one"):
    print("That's sad")
else:
    print("Is the cover of " + book + " " + color + "?")

music = input("What is your favorite kind of music? ")
if music == "sad":
    print("That's my favorite kind of music to!")
elif music == "Sad":
     print("That's my favorite kind of music to!")
elif music == "country":
    print("Why!?")
elif music == "Country":
     print("Why!?")
else:
    print(music + " is a grand type of music!")

poke = input("What's your favorite pokemon? ")
if poke == "Spheal":
    print(poke + " is my favorite pokemon to!")
elif poke == "spheal":
    print(poke + " is my favorite pokemon to!") 
elif poke == "Zora":
    print("Like the pre-evo of N?")
elif poke == "zora":
    print("Like the pre-evo of N?")
elif poke == "Zorark":
    print(poke + " is a really fun ghost type!")
elif poke == "zorark":
     print(poke + " is a really fun ghost type!")
elif poke == "Gardavoir" or "L":
    print(". . .")
else :
    print(poke + "is an amazing pokemon!")
