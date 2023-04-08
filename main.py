import random

import typer

from typing import Optional

from rich import print
from rich.console import Console
from rich.table import Table


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
def hello(name: str, lastname: str = ""):
    """Greets the user"""
    print(f'Hello {name} {lastname}')


@app.command()
def goodbye(name: str, lastname: str = "", formal: bool = False):
    """Says goodbye to the user"""
    if formal:
        print(f"Goodbye Mr. {name} {lastname}. Have a good day.")
    else:
        print(f"Bye {name} {lastname}!")


@app.command()
def printTable():
    """Prints a table"""
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


@app.command()
def printMarkup():
    """Demonstrates how markup can be printed"""
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def getData():
    """Prints out data colored"""
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
def createUser(username: str):
    maybe_create_user(username)


@app.command()
def optionalArg(name: Optional[str] = typer.Argument(None)):
    """Demonstrates optional arguments"""
    if name is None:
        print("Hello World")
    else:
        print(f"Hello {name}")


def get_random_name():
    return random.choice(['John', 'Jane', 'Jack', 'Jennifer', 'Joe', 'Juliette'])


@app.command()
def dynamicArg(name: str = typer.Argument(get_random_name, help="The random name that will be generated")):
    """This command will generate a random name"""
    print(f"The current random name is [cyan]{name}[/cyan]")


@app.command()
def greet(name: Optional[str] = typer.Argument('World', metavar="✨username✨", help="Who to greet", show_default=True)):
    """Say hi to NAME politely"""
    print(f"Hello {name}")


@app.command()
def secondaryArgs(name: str = typer.Argument(..., help="Who to greet", show_default=False),
                  lastname: str = typer.Argument("", help="The last name", hidden=False, rich_help_panel="Secondary Arguments"),
                  age: int = typer.Argument(0, help="The user's age", show_default=False, rich_help_panel="Secondary Arguments")):
    print(f"{name} {lastname} ({age})") 


@app.command()
def envVars(day: str = typer.Argument(..., envvar='TODAY', help='If DAY is ommitted, value comes from envvar TODAY', show_default=False, show_envvar=True)):
    """Demonstrates envvar functionality"""
    print(f"Today is {day}")


if __name__ == "__main__":
    app()
