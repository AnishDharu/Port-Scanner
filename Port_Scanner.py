import socket
import termcolor

# Dictionary of common ports and their corresponding service names
port_services = {
    20: 'FTP-DATA',
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    67: 'DHCP',
    68: 'DHCP',
    69: 'TFTP',
    80: 'HTTP',
    110: 'POP3',
    123: 'NTP',
    143: 'IMAP',
    161: 'SNMP',
    194: 'IRC',
    443: 'HTTPS',
    3306: 'MySQL',
    3389: 'RDP',
    8080: 'HTTP-ALT'
    # Add more if needed
}

def scan(target, ports):
    print(termcolor.colored(f"\n[*] Starting Scan for {target}\n", "green"))
    for port in range(1, ports + 1):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        service = port_services.get(port, "Unknown Service")
        print(termcolor.colored(f"[+] Port {port} ({service}) is OPEN", "cyan"))
        sock.close()
    except:
        pass

# Main input section
targets = input("[*] Enter the target(s) to scan (split with commas if multiple): ")
ports = int(input("Enter the number of ports to scan (e.g., 1000): "))

if ',' in targets:
    print(termcolor.colored("[*] Scanning multiple targets...\n", "yellow"))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(), ports)
else:
    scan(targets.strip(), ports)
