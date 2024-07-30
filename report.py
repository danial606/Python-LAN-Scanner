import json

def save_report(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    sample_data = {
        "network": "192.168.1.0/24",
        "alive_hosts": ["192.168.1.1", "192.168.1.2"],
        "clients": [
            {"ip": "192.168.1.1", "mac": "00:11:22:33:44:55"},
            {"ip": "192.168.1.2", "mac": "66:77:88:99:AA:BB"}
        ],
        "open_ports": {
            "192.168.1.1": [22, 80],
            "192.168.1.2": [21, 23]
        }
    }
    save_report(sample_data)
    print("Report saved as report.json")
