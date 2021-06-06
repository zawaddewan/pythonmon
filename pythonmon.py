import time

def lowercase(s):
    newstring = ''
    i = 0
    while i < len(s):
        if s[i] >= 'A' and s[i] <= 'Z':
            newstring += chr(ord(s[i]) + 32)
        else:
            newstring += s[i]
        i += 1
    return newstring

logofile = open('logo2.txt')
logo = logofile.read()

def gamestart():
    print(logo)
    time.sleep(1)
    print('> Play')
    print('> Credits')
    option = lowercase(input())
    if option ==  'credits':
        print('Charizard ASCII art: https://www.asciiart.eu/video-games/pokemon')
        while option != 'play':
            option = lowercase(input())
    if option == 'play':
        print('Welcome to the World of Pythonmon!')
        time.sleep(1)
        print('Select your Pokemon:')
        
gamestart()
    