import tkinter as tk
from tkinter import scrolledtext
from lan_scanner import main as lan_scan

class ScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LAN Scanner")

        self.network_label = tk.Label(root, text="Network:")
        self.network_label.pack()
        self.network_entry = tk.Entry(root)
        self.network_entry.pack()

        self.port_label = tk.Label(root, text="Ports (e.g., 1-1024):")
        self.port_label.pack()
        self.port_entry = tk.Entry(root)
        self.port_entry.pack()

        self.scan_button = tk.Button(root, text="Scan", command=self.scan)
        self.scan_button.pack()

        self.result_text = scrolledtext.ScrolledText(root, width=80, height=20)
        self.result_text.pack()

    def scan(self):
        network = self.network_entry.get()
        ports = self.port_entry.get()
        lan_scan(network, ports)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScannerApp(root)
    root.mainloop()
