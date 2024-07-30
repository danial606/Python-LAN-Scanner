import nmap

def os_service_detection(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, arguments="-O -sV")
    os_info = nm[ip]['osmatch'][0] if 'osmatch' in nm[ip] and nm[ip]['osmatch'] else None
    services = {}
    if 'tcp' in nm[ip]:
        for port in nm[ip]['tcp']:
            service = nm[ip]['tcp'][port]
            services[port] = {
                'name': service['name'],
                'product': service.get('product'),
                'version': service.get('version')
            }
    return os_info, services

if __name__ == "__main__":
    ip = input("Enter the IP to scan for OS and services: ")
    os_info, services = os_service_detection(ip)
    print(f"OS Info: {os_info}")
    print("Services:")
    for port, service in services.items():
        print(f"Port {port}: {service}")