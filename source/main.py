import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import threading
import argparse
import os
import sys

log_text = None
device_combo = None
apk_listbox = None

# Log output to GUI and console
def log_output(msg):
    print(msg)
    if log_text:
        log_text.insert(tk.END, msg + '\n')
        log_text.see(tk.END)

# Fetch connected devices
def get_connected_devices():
    try:
        result = subprocess.check_output(['adb', 'devices'], encoding='utf-8')
        devices = []
        for line in result.splitlines()[1:]:
            if line.strip() and 'device' in line:
                parts = line.split()
                devices.append(parts[0])
        return devices
    except Exception:
        return []

# Install APKs
def install_apks(device, apk_paths):
    for apk in apk_paths:
        try:
            result = subprocess.run(['adb', '-s', device, 'install', '-r', apk],
                                    check=True, capture_output=True, text=True)
            log_output(f"[✓] Installed {os.path.basename(apk)} on {device}")
        except subprocess.CalledProcessError as e:
            log_output(f"[✗] Failed to install {os.path.basename(apk)} on {device}\n{e.stderr.strip()}")

# Browse for APKs
def browse_apks():
    file_paths = filedialog.askopenfilenames(filetypes=[("APK files", "*.apk")])
    if file_paths:
        apk_listbox.delete(0, tk.END)
        for path in file_paths:
            apk_listbox.insert(tk.END, path)

# Refresh device list
def refresh_devices():
    device_combo['values'] = get_connected_devices()

# Threaded install button
def threaded_install():
    device = device_combo.get()
    apks = apk_listbox.get(0, tk.END)
    if not device or not apks:
        messagebox.showwarning("Missing Info", "Select a device and at least one APK.")
        return
    threading.Thread(target=install_apks, args=(device, apks)).start()

# Connect via IP and optional pairing code
def connect_device(ip_port=None, pairing_code=None):
    try:
        if ip_port and pairing_code:
            subprocess.run(['adb', 'pair', ip_port, pairing_code], check=True)
            log_output(f"[✓] Paired with device: {ip_port}")
        elif ip_port:
            subprocess.run(['adb', 'connect', ip_port], check=True)
            log_output(f"[✓] Connected to device: {ip_port}")
        else:
            log_output("No IP:Port provided.")
        refresh_devices()
    except subprocess.CalledProcessError as e:
        log_output(f"[✗] Failed to connect: {e.stderr.strip()}")

# New window to add a device
def open_add_device_window():
    def connect_action():
        ip_port = ip_entry.get().strip()
        pairing_code = code_entry.get().strip()
        threading.Thread(target=connect_device, args=(ip_port, pairing_code if pairing_code else None)).start()

    add_window = tk.Toplevel()
    add_window.title("Add ADB Device")

    ttk.Label(add_window, text="IP:Port").grid(row=0, column=0, padx=5, pady=5)
    ip_entry = ttk.Entry(add_window, width=30)
    ip_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(add_window, text="Pairing Code (optional)").grid(row=1, column=0, padx=5, pady=5)
    code_entry = ttk.Entry(add_window, width=30)
    code_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(add_window, text="Connect", command=connect_action).grid(row=2, column=0, columnspan=2, pady=10)

# GUI launcher
def run_gui():
    global device_combo, apk_listbox, log_text

    root = tk.Tk()
    root.title("ADB APK Installer Tool")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Select Device:").grid(row=0, column=0, sticky=tk.W)
    device_combo = ttk.Combobox(frame, width=40)
    device_combo.grid(row=0, column=1, sticky=tk.W)
    ttk.Button(frame, text="Refresh", command=refresh_devices).grid(row=0, column=2, padx=5)
    ttk.Button(frame, text="Add Device", command=open_add_device_window).grid(row=0, column=3, padx=5)

    ttk.Label(frame, text="APK Files:").grid(row=1, column=0, sticky=tk.NW)
    apk_listbox = tk.Listbox(frame, height=6, width=60, selectmode=tk.MULTIPLE)
    apk_listbox.grid(row=1, column=1, columnspan=3, pady=5)

    ttk.Button(frame, text="Browse APKs", command=browse_apks).grid(row=2, column=1, sticky=tk.W)
    ttk.Button(frame, text="Install to Device", command=threaded_install).grid(row=2, column=2)

    ttk.Label(frame, text="Log:").grid(row=3, column=0, sticky=tk.NW)
    log_text = tk.Text(frame, height=10, width=90)
    log_text.grid(row=3, column=1, columnspan=3, pady=10)

    refresh_devices()
    root.mainloop()

# CLI mode handler
def cli_mode(args):
    if args.devices:
        devices = get_connected_devices()
        if devices:
            print("Connected ADB devices:")
            for dev in devices:
                print("  -", dev)
        else:
            print("No ADB devices found.")
    if args.install and args.device and args.apk:
        install_apks(args.device, args.apk)
    sys.exit(0)

# Main entry
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ADB APK Installer - GUI + CLI")
    parser.add_argument("--devices", action="store_true", help="List connected ADB devices")
    parser.add_argument("--device", help="ADB device ID (use with --install)")
    parser.add_argument("--apk", nargs='+', help="Path(s) to APK files (use with --install)")
    parser.add_argument("--install", action="store_true", help="Install APK(s) to device")

    if len(sys.argv) > 1:
        args = parser.parse_args()
        cli_mode(args)
    else:
        run_gui()
