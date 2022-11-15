# Import Libraries
from random_word import RandomWords
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Print Logo
print(Fore.RED+"        .__         _____.__  __             ")
print(Fore.RED+"  _____ |__| ______/ ____|___/  |_ ______    ")
print(Fore.RED+" /     \|  |/  ___\   __\|  \   __/  ___/    ")
print(Fore.RED+"|  Y Y  |  |\___ \ |  |  |  ||  | \___ \     ")
print(Fore.RED+"|__|_|  |__/____  >|__|  |__||__|/____  > /\ ")
print(Fore.RED+"      \/        \/                    \/  \/")
print(Fore.RED+" ")
print(Fore.RED+"Powered by RandomWords // Created by themisfits.ml")
print(Fore.RED+" ")

# Return a single random word
r = RandomWords()
final = r.get_random_word()
print("Heres your word: " + Fore.RED + final)