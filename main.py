import random
import time

import typer

from typing import Optional

from rich import print
from rich.console import Console
from rich.table import Table


__version__ = "0.1.0"

app = typer.Typer()
console = Console()

data = {
        "name": "Rick",
        "age": 42,
        "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
        "active": True,
        "affilation": None,
}

existing_usernames = ["rick", "morty"]


@app.command()
def say_hello(name: str, lastname: str = ""):
    """Greets the user"""
    print(f'Hello {name} {lastname}')


@app.command()
def say_goodbye(name: str, lastname: str = "", formal: bool = False):
    """Says goodbye to the user"""
    if formal:
        print(f"Goodbye Mr. {name} {lastname}. Have a good day.")
    else:
        print(f"Bye {name} {lastname}!")


@app.command()
def print_table():
    """Prints a table"""
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


@app.command()
def print_markup():
    """Prints markup"""
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def get_data():
    """Prints colored data"""
    print("Here's the data")
    print(data)


def maybe_create_user(username: str):
    if username == "root":
        print("The root user is reserved")
        raise typer.Abort()

    if username in existing_usernames:
        print("User already exists")
        raise typer.Exit(code=1)
    else:
        print(f"User created: {username}")
        send_new_user_notification(username)


def send_new_user_notification(username: str):
    print(f"Notification sent for user: {username}")


@app.command()
def create_user(username: str):
    """Creates a user if doesn't exist"""
    maybe_create_user(username)


@app.command()
def demo_optional_arguments(name: Optional[str] = typer.Argument(None)):
    """Demo for optional arguments"""
    if name is None:
        print("Hello World")
    else:
        print(f"Hello {name}")


def get_random_name():
    return random.choice(['John', 'Jane', 'Jack', 'Jennifer', 'Joe', 'Juliette'])


@app.command()
def demo_dynamic_arguments(name: str = typer.Argument(get_random_name, help="The random name that will be generated")):
    """Demo for dynamic arguments"""
    print(f"The current random name is [cyan]{name}[/cyan]")


@app.command()
def demo_metavar(name: Optional[str] = typer.Argument('World', metavar="✨username✨", help="Who to greet", show_default=True)):
    """Demo for metavar"""
    print(f"Hello {name}")


@app.command()
def demo_secondary_panel(name: str = typer.Argument(..., help="Who to greet", show_default=False),
                  lastname: str = typer.Argument("", help="The last name", hidden=False, rich_help_panel="Secondary Arguments"),
                  age: int = typer.Argument(0, help="The user's age", show_default=False, rich_help_panel="Secondary Arguments")):
    """Demo for secondary panel"""
    print(f"{name} {lastname} ({age})") 


@app.command()
def demo_envvars(day: str = typer.Argument(..., envvar='TODAY', help='If DAY is ommitted, value comes from envvar TODAY', show_default=False, show_envvar=True)):
    """Demo for envvars"""
    print(f"Today is {day}")


@app.command()
def demo_options(name: str = typer.Argument(..., help="Who to greet.", show_default=False),
            lastname: str = typer.Option("", "--formal", "-f", help="Last name of the person to greet."),
            formal: bool = typer.Option(False, help="Say hi formally."),
            debug: bool = typer.Option(..., help="Enable debugging.", 
            prompt="Please indicate whether you want to enable debug mode" # prompt=True
            )
            ):
    """
    Say hi to NAME, optionally with a --lastname.
    
    If --formal is used, day hi very formally.
    """
    if debug:
        print("Debug mode enabled.")
    else:
        print("Debug mode disabled.")

    if formal:
        print(f"Good day Mr. {name} {lastname}.")
    else:
        print(f"Hello {name} {lastname}")


@app.command()
def delete_project(project_name: str = typer.Option(..., prompt=True, confirmation_prompt=True)):
    print(f"Deleting project [pink]{project_name}[/pink]...")
    time.sleep(1.5)
    print(f"Project [pink]{project_name}[/pink] has been successfully deleted!")


@app.command()
def register_account(email: str = typer.Option(..., show_default=False, help="User's email address", prompt=True),
                     password: str = typer.Option(..., show_default=False, help="Passfor for the new account", prompt=True, confirmation_prompt=True, hide_input=True)):
    print(f"Your account ([magenta]{email}[/magenta]) has been successfully registered!")


@app.command()
def demo_option_name(username: str = typer.Option(..., "--name", "-n", show_default=False, help="User's name"), 
                     debug: bool = typer.Option(False, "--debug", "-d", help="Enable/disable debug mode")):
    if(debug):
        print("Debug mode is enabled.")
    else:
        print("Debug mode is disabled.")

    print(f"Hello {username}")


def name_callback(name: str):
    if name != 'Morzsi':
        raise typer.BadParameter("Only Morzsi is allowed!")
    return name


def version_callback(value: bool):
    if value:
        print(f"Current version: {__version__}")
        raise typer.Exit()


@app.command()
def demo_callback(name: str = typer.Option(..., prompt=True, callback=name_callback)):
    print(f"Hello {name}")


@app.command()
def demo_version(name: str = typer.Option(..., callback=name_callback), 
                 version: Optional[bool] = typer.Option(None, "--version", "-v", callback=version_callback, is_eager=True)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
