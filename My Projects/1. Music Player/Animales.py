from playsound import playsound

print("Cat, Dog, Lion, Wolf ")
print("IF you want to play all animal Voice Enter = All")
i = input("Which Animal voice You Want hear:")

class domestic_animals():
    def cat():
        playsound('C:/Users/mayyu/Documents/All-Refference-Code/Data/Music/cat.wav')

    def dog():
        playsound('C:/Users/mayyu/Documents/All-Refference-Code/Data/Music/Dog.wav')

    if i.lower() == "cat":
        cat()
    elif i.lower() == "dog":
        dog()
    elif i.lower() == "all":
        cat()
        dog()
   
class Wild_animals():
    def lion():
        playsound('C:/Users/mayyu/Documents/All-Refference-Code/Data/Music/lion.wav')
    def wolf():
        playsound('C:/Users/mayyu/Documents/All-Refference-Code/Data/Music/wolf.wav')

    if i.lower() == "lion":
          lion()
    elif i.lower() == "wolf":
        wolf()
    elif i.lower() == "all":
        lion()
        wolf()        
    else:
        print("Please enter Proper animal name")
    