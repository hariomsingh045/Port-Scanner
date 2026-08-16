# NEXUSSCAN

### Lightweight Command-Line TCP Port Scanner

NEXUSSCAN is a lightweight command-line TCP port scanner written in Python. It is designed for authorized security testing, cybersecurity labs, network reconnaissance, and educational purposes.

The tool accepts an IP address, domain name, or URL and can scan individual ports, multiple ports, or custom port ranges.

## Features

- TCP port scanning
- Multithreaded scanning
- IP address support
- Domain name resolution
- URL target support
- Custom port selection
- Port range scanning
- TCP service detection
- Colored terminal output
- Verbose mode
- Lightweight single-file implementation
- Command-line interface

## Requirements

- Python 3
- Linux / Kali Linux / macOS / Windows
- Network access to an authorized target

No external Python packages are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/hariom045418/Port-Scanner.git
cd Port-Scanner
```

Make the script executable:

```bash
chmod +x nexusscan.py
```

## Usage

### Basic Scan

By default, NEXUSSCAN scans ports 1-1000.

```bash
python3 nexusscan.py -t 127.0.0.1
```

### Custom Port Range

```bash
python3 nexusscan.py -t 127.0.0.1 -p 1-10000
```

### Specific Ports

```bash
python3 nexusscan.py -t 127.0.0.1 -p 22,80,443,8080
```

### Scan a Domain

```bash
python3 nexusscan.py -t example.com
```

### Scan a URL

```bash
python3 nexusscan.py -t http://127.0.0.1:8080
```

If the URL contains an explicit port, NEXUSSCAN automatically extracts and scans that port.

### Verbose Mode

```bash
python3 nexusscan.py -t 127.0.0.1 -v
```

## Command-Line Options

| Option | Description |
|---|---|
| `-t, --target` | Target IP address, domain, or URL |
| `-p, --ports` | Port, port list, or port range |
| `-v, --verbose` | Display additional scan information |
| `-h, --help` | Display help information |

## Example Output

```text
[*] Target: 127.0.0.1
[*] Scanning 1000 ports...

PORT     STATE      SERVICE
---------------------------------------------
1716     OPEN       UNKNOWN
8080     OPEN       HTTP-ALT

[+] Open ports: 2
[*] Time: 0.15s
```

## How It Works

NEXUSSCAN follows a simple reconnaissance workflow:

```text
Target
   |
   v
Target Parsing
   |
   v
Host Resolution
   |
   v
Port Selection
   |
   v
TCP Port Scanning
   |
   v
Service Detection
   |
   v
Scan Results
```

For each selected port, NEXUSSCAN attempts to establish a TCP connection.

```text
TCP Connection
       |
       +------ Connection successful ---> OPEN
       |
       +------ Connection failed -------> CLOSED
```

Multiple ports are scanned concurrently to improve performance.

## Technologies

NEXUSSCAN uses Python's standard library:

- Python 3
- `socket`
- `argparse`
- `threading`
- `concurrent.futures`
- `urllib.parse`

No third-party Python dependencies are required.

## Project Structure

```text
Port-Scanner/
│
├── nexusscan.py
└── README.md
```

## Learning Objectives

This project demonstrates practical understanding of:

- TCP/IP networking
- Socket programming
- Port scanning
- Network reconnaissance
- DNS/hostname resolution
- Service identification
- Multithreading
- Python exception handling
- Command-line application development

## Responsible Use

NEXUSSCAN is intended only for:

- Authorized penetration testing
- Cybersecurity laboratories
- CTF environments
- Educational purposes
- Systems owned by the user
- Systems where explicit permission has been granted

**Do not scan systems or networks without authorization.**

The developer is not responsible for misuse of this tool.

## Author

### Hariom Singh

Cybersecurity & Computer Science Engineering Student

**Email:** hariomsingh28453@gmail.com

**GitHub:** https://github.com/hariom045418

**LinkedIn:** https://www.linkedin.com/in/hariom-singh-75244b328/

## Future Improvements

Possible future improvements:

- Improved service detection
- Banner grabbing
- Scan result export
- JSON/CSV reporting
- IPv6 support
- Better filtered-port detection
- Configurable scanning parameters
- Progress indicators

## License

This project is intended for educational and authorized security testing purposes.
