import typer

import pfp_cli.enum as enum
import pfp_cli.scan as scan

app = typer.Typer()
app.add_typer(enum.app, name="enum")
app.add_typer(scan.app, name="scan")


if __name__ == "__main__":
    app()
