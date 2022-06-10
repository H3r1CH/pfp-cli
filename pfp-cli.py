import typer
import requests

app = typer.Typer()
enum_app = typer.Typer()
app.add_typer(enum_app, name="enum")
scan_app = typer.Typer()
app.add_typer(scan_app, name="scan")


@enum_app.command('dir')
def dir(url: str = typer.Argument(..., help="URL to bust"), 
    file: typer.FileText = typer.Argument(..., help="Wordlist to use"),
    ext: str = typer.Argument("", help="File Extension")):

    for f in file:
        enum_dir = f"{url}/{f}".strip() + f"{ext}"
        #print(enum_dir)
        r = requests.get(enum_dir)
        print(r.url)
        if r.status_code==404:
            pass
        else:
            print("Valid directory: ", enum_dir, r.status_code)


@enum_app.command('sub')
def sub(url: str = typer.Argument(..., help="Subdomain to bust"),
    file: typer.FileText = typer.Argument(..., help="Wordlist to use"),
    sec: str = typer.Argument(None, help="For HTTPS")):

    for f in file:
        if sec:
            enum_sub = f"https://{f}".strip() + f".{url}"
            print(enum_sub)
        else:
            enum_sub = f"http://{f}".strip() + f".{url}"
            print(enum_sub)
    #typer.echo(f"Busting... {file}.{url}")


@scan_app.command('net')
def scan(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


if __name__ == "__main__":
    app()
