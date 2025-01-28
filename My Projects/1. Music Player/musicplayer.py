from playsound import playsound
#playsound('C:\\Users\\mayyu\\Downloads\\1.mp3') 

'''
Alternative of Playsound

import pygame
pygame.mixer.init()
pygame.mixer.music.load('C:\\Users\\mayyu\\Downloads\\2.mp3')
pygame.mixer.music.play()
input("Press Enter to exit...")
'''

music = input("Enter Between 1 to 5  Music You want to play :")

if "1" in music:
    print("Music Number 1 is Runnig...")
    playsound('C:\\Users\\mayyu\\Music\\Musics\\1.mp3')   
elif "2" in music:
    print("Music Number 2 is Runnig...")
    playsound('C:\\Users\\mayyu\\Music\\Musics\\2.mp3')
elif "3" in music:
    print("Music Number 3 is Runnig...")
    playsound('C:\\Users\\mayyu\\Music\\Musics\\3.mp3')
elif "4" in music:
    print("Music Number 4 is Runnig...")
    playsound('C:\\Users\\mayyu\\Music\\Musics\\4.mp3')
elif "5" in music:
    print("Music Number 5 is Runnig...")
    playsound('C:\\Users\\mayyu\\Music\\Musics\\5.mp3')
else:
    print("Enter Number Between 1 to 5")
