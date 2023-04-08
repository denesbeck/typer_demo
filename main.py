import typer
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
    print(f'Hello {name} {lastname}')


@app.command()
def goodbye(name: str, lastname: str = "", formal: bool = False):
    if formal:
        print(f"Goodbye Mr. {name} {lastname}. Have a good day.")
    else:
        print(f"Bye {name} {lastname}!")


@app.command()
def printTable():
    table = Table("Name", "Item")
    table.add_row("Rick", "Portal Gun")
    table.add_row("Morty", "Plumbus")
    console.print(table)


@app.command()
def printMarkup():
    print("[bold red]Alert![/bold red] [green]Portal gun[/green] shooting! :boom:")


@app.command()
def getData():
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


if __name__ == "__main__":
    app()
