import typer
from scapy.all import ARP, Ether, srp

app = typer.Typer()

@app.command('arp')
def arp(ipaddr: str = typer.Argument(..., help="Specify the Target IP address"), 
    mask: str = typer.Argument("24", help="Specify the Subnet mask."),
    interface: str = typer.Argument("eth0", help="Specify the Interface."),
    brdcstmac: str = typer.Argument("ff:ff:ff:ff:ff:ff", help="")):
    
    # Specify the target address
    target = f"{ipaddr}/{mask}"
    #  Discover hosts on a local ethernet network using the ARP Ping method
    ans, unans = srp(Ether(dst=brdcstmac)/ARP(pdst=target), timeout=2)

    for sent, received in ans:
        print (received.sprintf(r"%Ether.src% - %ARP.psrc%"))


@app.command('ping')
def ping(interface: str = typer.Argument(..., help="Specify the Interface e.g. eth0"),
    ipaddr: str = typer.Argument(..., help="Specify the Target IP address"), 
    subnet: str = typer.Argument(..., help="Specify the Subnet e.g. /24"),
    brdcstmac: str = typer.Argument(..., help="Specify the Subnet e.g. /24")):
    
    # Specify the target address
    target = f"{ipaddr}/{subnet}"
    # Create ARP packet
    arp = ARP(pdst=target)

    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=f"target"), timeout=2)


@app.command('port')
def port(interface: str = typer.Argument(..., help="Specify the Interface e.g. eth0"),
    ipaddr: str = typer.Argument(..., help="Specify the Target IP address"), 
    subnet: str = typer.Argument(..., help="Specify the Subnet e.g. /24"),
    brdcstmac: str = typer.Argument(..., help="Specify the Subnet e.g. /24")):
    
    # Specify the target address
    target = f"{ipaddr}/{subnet}"
    # Create ARP packet
    arp = ARP(pdst=target)

    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=f"target"), timeout=2)


if __name__ == "__main__":
    app()
