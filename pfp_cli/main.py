import typer

import pfp_cli.enum as enum
import pfp_cli.scan as scan

app = typer.Typer()
app.add_typer(enum.app, name="enum")
app.add_typer(scan.app, name="scan")


__version__ = "0.1.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"PFP-CLI Version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(version: bool = typer.Option(None, "-v", "--version", 
callback=version_callback, is_eager=True, help="Show current version of pfp-cli")):
    return


if __name__ == "__main__":
    app()
