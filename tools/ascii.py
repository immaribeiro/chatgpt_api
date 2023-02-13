import requests
import os

from pyfiglet import Figlet
from termcolor import cprint, colored
from time import sleep


def ascii(text, font, color, width):
    #instantiating the Figlet() class
    if font is not None and width is not None:
        f = Figlet(font=font, width=width )
    else:
        color = 'white'
        f = Figlet(font='banner3-D', width=100 )
    #this prints a customizable ascii art
    art_str = f.renderText(text)
    
    cprint(art_str, color) #, attrs=["bold", "blink"])
    
    return art_str

text = 'ChatGPT'

def print_all_fonts(text):
    URL = "https://gist.githubusercontent.com/Technetium1/f97474f52096303d556963d37f59edee/raw/38f9689f5125364b1e46135b97f7272242c601ef/pyfigletfonts.txt"
    response = requests.get(URL)
    open("tools/pyfigletfonts.txt", "wb").write(response.content)

    with open('tools/pyfigletfonts.txt', "r") as file:
        fonts = file.read().splitlines()

    os.makedirs('tools/output', exist_ok=True)
    with open('tools/output/' + 'fonts_test.txt', 'a', encoding='utf-8') as f2:
       
        for fonty in fonts:
            print("Testing font " + fonty)
            f = Figlet(font=fonty, width=80)
            file = f.renderText(text)
            f2.write('\nTesting font ' + fonty + '\n' + file + '\n')

            print(f.renderText(text))
            # sleep(0.8)
