

# ADB APK Installer Tool

A modern, user-friendly tool for installing APK files on Android devices via ADB (Android Debug Bridge). This application offers both a **Graphical User Interface (GUI)** and a **Command Line Interface (CLI)**, making it versatile for developers, testers, and enthusiasts.

---

## 🚀 Features

- **Graphical Interface**:
  - Select and install multiple APKs with a few clicks.
  - Connect to devices via USB or wirelessly (IP-based with optional pairing code).
  - Real-time log output for installation status.
  - Refreshable device list for easy device management.
  - Browse and select APK files effortlessly.

- **Command Line Interface**:
  - List connected ADB devices.
  - Install APKs to a specified device with minimal commands.

- **Cross-Platform**:
  - Works on Windows, macOS, and Linux (requires ADB installed).

- **Threaded Operations**:
  - Non-blocking installation process to keep the GUI responsive.

---

## 📋 Prerequisites

- **ADB (Android Debug Bridge)** installed and added to your system's PATH.
- **Python 3.6+** with the following packages:
  - `tkinter` (usually included with Python)
  - `pyinstaller` (for creating executable files, optional)

Install dependencies using:
```bash
pip install pyinstaller
```

---

## 🛠️ Installation

1. **Clone or Download**:
   - Clone this repository or download the source code.
   ```bash
   git clone https://github.com/your-username/adb-apk-installer.git
   ```

2. **Run the Script**:
   - Execute the Python script directly:
   ```bash
   python ADB-PKG-INSTALLER.py
   ```

3. **Build Executable (Optional)**:
   - Create a standalone executable using PyInstaller:
   ```bash
   pyinstaller --onefile ADB-PKG-INSTALLER.py
   ```
   - Find the executable in the `dist/` folder.

---

## 🎮 Usage

### GUI Mode
1. Run the script without arguments:
   ```bash
   python ADB-PKG-INSTALLER.py
   ```
2. Select a connected device from the dropdown or add a device via IP.
3. Browse and select APK files.
4. Click **Install to Device** to start the installation.
5. View the installation progress in the log window.

### CLI Mode
- **List connected devices**:
  ```bash
  python ADB-PKG-INSTALLER.py --devices
  ```
- **Install APKs to a device**:
  ```bash
  python ADB-PKG-INSTALLER.py --install --device <device_id> --apk <path_to_apk1> <path_to_apk2>
  ```
  Example:
  ```bash
  python ADB-PKG-INSTALLER.py --install --device emulator-5554 --apk app1.apk app2.apk
  ```

---

## 📸 Screenshots

![GUI Screenshot](https://via.placeholder.com/600x400.png?text=GUI+Screenshot)
*Main GUI showing device selection and APK installation.*

---

## 🐛 Troubleshooting

- **ADB not found**: Ensure ADB is installed and added to your PATH.
- **No devices listed**: Check USB debugging is enabled on your Android device or verify IP/port for wireless connections.
- **Installation failures**: Confirm the APK is compatible with the target device and check the log for error details.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add YourFeature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Built with [Python](https://www.python.org/) and [Tkinter](https://docs.python.org/3/library/tkinter.html).
- Inspired by the need for a simple, cross-platform ADB tool.

---

*Made with ❤️ by [AHMED BHAI](https://github.com/ahmedsalim91)*

