import time # Proives the facilite to make the program sleep 
import string # Provides the predefined character sets 
import getpass # Allows the user to enter the password without visible in the screen 
import math # Used to calculate password entropy for strength evaluation 
import typer # For building CLI supported functions
import yaml # Importing the rich Config for consistent output
from rich.theme import Theme # Importing the theme
from rich.console import Console # Importing the console for console output
from rich.table import Table # Importing table to create the result table
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn # Importing inorder to create a progress bar 
from pathlib import Path # Impoort path for importing config

app = typer.Typer()
 # Initializing the config
BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "rich_config.yaml"
with open(CONFIG_PATH) as f: 
    config = yaml.safe_load(f)


# Creating a custom theme : 
custom_theme = Theme({
    "primary": config["theme"]["primary"],
    "success": config["theme"]["success"],
    "warning": config["theme"]["warning"],
    "error": config["theme"]["error"],
})

console = Console(theme=custom_theme) # Initializing the console using that theme

MIN_LENGTH = 8

def calculate_entropy(password): 
    """Calculates the entropy based on the character diversity and size"""
    charset_size = 0
    if any(c in string.ascii_lowercase for c in password): 
        charset_size += 26 
    if any(c in string.ascii_uppercase for c in password): 
        charset_size +=26
    if any(c in string.digits for c in password): 
        charset_size += 10 
    if any(c in string.punctuation for c in password): 
        charset_size += len(string.punctuation)
    if any(c.isspace() for c in password): 
        charset_size += 1 

    return len(password) * math.log2(charset_size) if charset_size else 0


def check_password_strength(): 
    password = getpass.getpass('Enter your password: ')
    
    if len(password) < MIN_LENGTH : 
        console.print(f"Your password is too short ! The minimum password length must be {MIN_LENGTH}\n", style="error")
        return 
    
    entropy = calculate_entropy(password) 
    
    lower_count = sum(1 for c in password if c in string.ascii_lowercase)
    upper_count = sum(1 for c in password if c in string.ascii_uppercase)
    num_count = sum(1 for c in password if c in string.digits)
    punc_count = sum(1 for c in password if c in string.punctuation)
    space_count = sum(1 for c in password if c.isspace())


    # Classifying password strength : 
    if entropy < 26 : 
        remarks = "Very weak password. Change it immediately"
        remark_style = "error"
    elif entropy < 36:
        remarks = "Weak: Can be cracked quickly. Use a stronger password."
        remark_style = "error"
    elif entropy < 60:
        remarks = "Moderate: Decent password, but can still be improved."
        remark_style = "warning"
    elif entropy < 80:
        remarks = "Strong: Hard to guess, but consider making it longer."
        remark_style = "success"
    else:
        remarks = "Very Strong: Excellent password! Highly secure."
        remark_style = "success"

    # Create a progress bar to showcase that the results are processing : 
    with Progress(
        TextColumn("[bold green]{task.description}"),
        BarColumn(bar_width=40),
        "[progress.percentage]{task.percentage:>3.0f}%", 
        TimeElapsedColumn(), 
        console=console
    ) as progress: 
        task = progress.add_task("Analyzing password....", total=100)

        while not progress.finished: 
            progress.update(task, advance=5)
            time.sleep(0.06)

    # Display password analysis : 

    # Create the table columns : 
    table = Table(title="Password Analysis")
    table.add_column("Lowercase Letters", style="cyan")
    table.add_column("Uppercase Letters", style="cyan")
    table.add_column("Numbers", style="cyan")
    table.add_column("Punctuation Count", style="cyan")
    table.add_column("Space Count", style="cyan")
    table.add_column("Entropy Score", style="magenta")
    
    # Create the response records : 
    table.add_row(str(lower_count), str(upper_count), str(num_count), str(punc_count), str(space_count), f"{entropy:.2f}")
    
    console.print(table)

    console.print(remarks, style = remark_style)

def check_another_password(): 
    """Asks if the user wants to check another password"""
    while True: 
        choice = input(" 🔄 Do you want to check another password ? (y/n): ").strip().lower()

        if choice == 'y': 
            return True 
        elif choice == 'n': 
            print("👋 Exiting... Stay secure!")
            return False
        else: 
            print("⚠️ Invalid input. Please enter 'y' or 'n'.")

@app.command()
def check_strength(once:bool = False): 
    console.print("===== 🔑 Welcome to Password Strength Checker 🔑 =====", style="success")
    if once: 
        check_password_strength()
    else: 
        while True: 
            check_password_strength()
            if not check_another_password(): 
                break

if __name__ ==  '__main__' : 
   app()


