from scapy.all import sr1, IP, ICMP, conf
import ipaddress

def ping_sweep(network):
    # Ensure L3 socket is configured for raw sockets
    conf.L3socket = conf.L3socket
    net = ipaddress.ip_network(network)
    alive_hosts = []

    for ip in net.hosts():
        resp = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)
        if resp:
            alive_hosts.append(str(ip))

    return alive_hosts
