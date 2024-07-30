import argparse
import threading
from ping_sweep import ping_sweep
from arp_scan import arp_scan
from port_scan import port_scan
from os_service_detection import os_service_detection
from report import save_report

def perform_ping_sweep(targets):
    print("Performing ping sweep...")
    alive_hosts = []
    for target in targets:
        alive_hosts.extend(ping_sweep(target))
    print("Alive hosts:")
    for host in alive_hosts:
        print(host)
    return alive_hosts

def perform_arp_scan(targets):
    print("\nPerforming ARP scan...")
    clients = []
    for target in targets:
        clients.extend(arp_scan(target))
    print("Available devices in the network:")
    for client in clients:
        print(f"IP: {client['ip']}, MAC: {client['mac']}")
    return clients

def perform_port_scan(host, ports_range, open_ports_dict):
    print(f"\nScanning ports on {host}...")
    open_ports = port_scan(host, ports_range)
    open_ports_dict[host] = open_ports
    print(f"Open ports on {host}:")
    for port in open_ports:
        print(port)

def perform_os_service_detection(host, os_services_info):
    print(f"\nDetecting OS and services on {host}...")
    os_info, services = os_service_detection(host)
    os_services_info[host] = {"os_info": os_info, "services": services}
    print(f"OS Info: {os_info}")
    print("Services:")
    for port, service in services.items():
        print(f"Port {port}: {service}")

def main(targets, ports):
    print(f"Performing LAN scan for targets {targets} and ports {ports}...")

    ping_sweep_thread = threading.Thread(target=perform_ping_sweep, args=(targets,))
    ping_sweep_thread.start()

    arp_scan_thread = threading.Thread(target=perform_arp_scan, args=(targets,))
    arp_scan_thread.start()

    ports_range = range(int(ports.split('-')[0]), int(ports.split('-')[1]) + 1)
    open_ports_dict = {}

    ping_sweep_thread.join()

    alive_hosts = perform_ping_sweep(targets)

    arp_scan_thread.join()

    clients = perform_arp_scan(targets)

    port_scan_threads = []
    for host in alive_hosts:
        thread = threading.Thread(target=perform_port_scan, args=(host, ports_range, open_ports_dict))
        port_scan_threads.append(thread)
        thread.start()

    os_service_threads = []
    os_services_info = {}
    for host in alive_hosts:
        thread = threading.Thread(target=perform_os_service_detection, args=(host, os_services_info))
        os_service_threads.append(thread)
        thread.start()

    for thread in port_scan_threads:
        thread.join()
    for thread in os_service_threads:
        thread.join()

    report_data = {
        "targets": targets,
        "alive_hosts": alive_hosts,
        "clients": clients,
        "open_ports": open_ports_dict,
        "os_services_info": os_services_info
    }
    save_report(report_data)
    print("Report saved as report.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAN Scanner")
    parser.add_argument("targets", nargs="+", help="IP addresses or network ranges to scan (e.g., 192.168.1.0/24, 192.168.1.1)")
    parser.add_argument("--ports", help="Ports to scan (e.g., 1-1024)", default="1-1024")
    args = parser.parse_args()

    main(args.targets, args.ports)
