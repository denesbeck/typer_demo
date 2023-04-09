import typer

app = typer.Typer(help="Awsome CLI user manager", rich_markup_mode="rich")


@app.command("create", help="[green]Create[/green] a new user with USERNAME. :sparkles:")
def create_user(username: str = typer.Option(..., help='Name of the user.', show_default=False)):
    print(f"Creating user {username}")


@app.command()
def delete(username: str, force: bool = typer.Option(..., "--force", "-f", prompt="Are you sure you want to delete this user?", help="Force deletion without confirmation.")):
    """
    [red]Delete[/red] a user with USERNAME. :fire:
    """
    if force:
        print(f"Deleting user: {username}.")
    else:
        print("Operation cancelled.")


@app.command(deprecated=True)
def delete_all(force: bool = typer.Option(..., "--force", "-f", prompt="Are you sure you want to delete ALL users?", help="Force deletion without confirmation.")):
    """
    [red]Delete[/red] ALL users in the database. :fire:
    """
    if force:
        print("Deleting ALL users.")
    else:
        print("Operation cancelled.")


@app.command()
def init():
    """
    [cyan]Initialize[/cyan] the users database. :computer:
    """
    print("Initializing user database.")


@app.command(rich_help_panel="Utils and Configs")
def config(configuration: str):
    """
    [blue]Configure[/blue] the system. :wrench:
    """
    print(f"Configuring the system with: {configuration}")


@app.command(rich_help_panel="Utils and Configs")
def sync():
    """
    [blue]Synchronize[/blue] the system or something fancy like that. :recycle:
    """
    print("Syncing the system")


@app.command(rich_help_panel="Help and Others")
def help():
    """
    Get [yellow]help[/yellow] with the system. :question:
    """
    print("Opening help portal...")


@app.command(rich_help_panel="Help and Others")
def report():
    """
    [yellow]Report[/yellow] an issue. :bug:
    """
    print("Please open a new issue online, not a direct message")


if __name__ == "__main__":
    app()
