from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Print text in different colors
print(Fore.RED + 'This is red text')
print(Fore.GREEN + 'This is green text')
print(Fore.YELLOW + 'This is yellow text')
print(Fore.BLUE + 'This is blue text')
print(Fore.MAGENTA + 'This is magenta text')
print(Fore.CYAN + 'This is cyan text')
print(Fore.WHITE + 'This is white text')

# Reset to default color
print(Style.RESET_ALL + 'This is default text color')
