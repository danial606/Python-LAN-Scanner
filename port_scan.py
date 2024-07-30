import socket

def port_scan(ip, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    ip = input("Enter the IP to scan: ")
    ports = range(1, 1025)  # Scanning ports 1-1024
    open_ports = port_scan(ip, ports)
    print(f"Open ports on {ip}:")
    for port in open_ports:
        print(port)
