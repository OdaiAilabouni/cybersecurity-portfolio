import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                sock.send(b'Hello\r\n')
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            sock.close()
            return True, banner
        sock.close()
        return False, None
    except Exception as e:
        return False, str(e)

def scan_host(host, start_port=20, end_port=1024):
    print(f"Scanning {host} for open ports {start_port} to {end_port}...")
    open_ports = {}
    for port in range(start_port, end_port + 1):
        is_open, banner = scan_port(host, port)
        if is_open:
            open_ports[port] = banner
            print(f"[+] Port {port} open: {banner}")
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter target host (IP or domain): ")
    open_ports_info = scan_host(target_host)
    print(f"\nScan complete. Open ports found: {len(open_ports_info)}")

