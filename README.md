# Python-LAN-Scanner
Small project I worked on which allows to scan devices on the local LAN. It utilizes various scanning techniques to find devices, open ports, and services running on those devices, and can also detect which operating system version its running on. Once run successfully you can expect it to really take a while to scan the network(Something I expect to make faster hopefully)
# Features
1.Ping Sweep: Identifies active hosts in the network.

2.ARP Scan: Discovers devices and their MAC addresses.

3.Port Scanning: Detects open ports and associated services.

4.OS and Service Detection: Identifies the operating systems and services running on the detected devices.

5.Report Generation: Outputs the scan results into a JSON report(Rudimentery Implementation)

# Requirements
1. Python 3.6+

2. scapy can be installed using

` pip install scapy
`

3. nmap

` pip install python-nmap
`

# Usage
Run the scanner using `python lan_scanner.py <network> --ports <port-range>`

An example input is 

`python lan_scanner.py 192.168.1.0/24 --ports 1-1024
`



