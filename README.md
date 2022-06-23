# pfp-cli
Python for Pentesters CLI inspired by the TryHackMe room Python for Pentesters.

## Installation
```bash
git clone https://github.com/H3r1CH/pfp-cli.git
cd pfp-cli
poetry install
```
### Help
```bash
pfp-cli --help
WARNING: No libpcap provider available ! pcap won't be used
Usage: pfp-cli [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version         Show current version of pfp-cli
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  enum
  scan
```

## Enumeration
```bash
pfp-cli enum --help
WARNING: No libpcap provider available ! pcap won't be used
Usage: pfp-cli enum [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  dir
  sub
```

### Directory Busting
```bash
pfp-cli enum dir --help
WARNING: No libpcap provider available ! pcap won't be used
Usage: pfp-cli enum dir [OPTIONS] URL FILE [EXT]

Arguments:
  URL    URL to bust  [required]
  FILE   Wordlist to use  [required]
  [EXT]  File Extension  [default: ]

Options:
  --help  Show this message and exit.
```
```bash
pfp-cli enum dir 10.10.10.1 wordlist.txt php
```

### Subdomain Busting

## Scanning
