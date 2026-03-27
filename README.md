# Computer-Information-Grabber
Computer Information Grabber - A comprehensive system information tool that displays CPU, RAM, Storage, OS, Battery, and Network details. Perfect for system monitoring and hardware diagnostics.



# Computer Information Grabber 💻

A comprehensive Python tool that displays detailed system information about your computer. Perfect for system monitoring, diagnostics, and hardware analysis.

## Features ✨

- 🖥️ **CPU Information** - Cores, threads, architecture, processor details
- 🧠 **RAM Information** - Total, used, available, free memory with percentages
- 💾 **Storage Information** - Disk partitions, usage statistics, free space
- 🪟 **OS Information** - Automatic Windows version detection (10, 11)
- 🔋 **Battery Detection** - Identifies Laptop vs Desktop/Workstation
- 🌐 **Network Information** - WiFi status and public IP address
- 🎨 **Beautiful Output** - ASCII art banners with colored text formatting

## System Information Displayed 📊

### Hardware Details
- CPU cores and threads
- System architecture (32-bit/64-bit)
- Processor model

### Memory Details
- Total RAM capacity
- RAM currently in use
- RAM usage percentage
- Available RAM
- Free RAM

### Storage Details
- Disk partitions and file systems
- Total storage capacity per drive
- Used storage space
- Free storage space

### Operating System
- Windows version detection (10/11)
- Build number
- Linux/Mac support

### Device Type
- Battery percentage (if laptop)
- Device classification (Laptop/Desktop)

### Network Status
- WiFi connection status
- Local IP address
- Connection diagnostics

## Installation 🚀

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Requirements

```bash
pip install psutil
pip install pyfiglet
pip install termcolor
```

Or install all at once:

```bash
pip install psutil pyfiglet termcolor
```

## Usage 🎯

### Basic Usage

```bash
python3 Computer_Information_Grabber.py
```

### What You'll See

```
========================================
COMPUTER INFORMATION GRABBER
========================================

========================================
HARDWARE INFORMATION
========================================

========================================
CPU INFORMATION
========================================

CPU: 8 Cores, 16 Threads

ARCHITECTURE: 64bit

PROCESSOR: Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz

========================================
RAM INFORMATON
========================================

RAM: 32.00GB

RAM USAGE: 8.54GB

RAM USAGE PERCENT: 26.7%

RAM AVAILABLE: 23.46GB

RAM FREE: 23.46GB

========================================
OPERATING SYSTEM INFORMATON
========================================

OPERATING SYSTEM: Windows 11

build: 10.0.22621.0

========================================
DISK INFORMATION
========================================

STORAGE PARTITIONS: C:\
FORMAT TYPE: NTFS

STORAGE C:\ DRIVE:476.84GB

STORAGE USAGE C:\ DRIVE:289.34GB

STORAGE FREE C:\ DRIVE:187.50GB

========================================
BATTERY INFORMATION
========================================

DEVICE: Desktop/Workstation

========================================
NETWORK INFORMATION
========================================

WIFI CONNECTION: Connected

COMPUTER IP ADDRESS: 192.168.1.100
```

## Code Structure 🏗️

### Main Functions

#### `line(text, extra_line="")`
- Creates formatted section headers
- Adds visual separation between sections
- Makes output clean and readable

#### `Banner(text, fonts, color)`
- Generates ASCII art banners
- Supports multiple font styles
- Color customization (yellow, blue, cyan, green, magenta, red)

### Information Gathering

1. **CPU Block** - Uses `psutil.cpu_count()` and `platform` module
2. **RAM Block** - Uses `psutil.virtual_memory()` for memory stats
3. **OS Block** - Uses `platform.version()` with Windows version detection
4. **Storage Block** - Uses `psutil.disk_partitions()` and `psutil.disk_usage()`
5. **Battery Block** - Uses `psutil.sensors_battery()` for battery info
6. **Network Block** - Uses `socket` module for IP detection

## How It Works 🔧

1. **Imports Libraries** - psutil, platform, socket, pyfiglet, termcolor
2. **Displays Banner** - Shows colorful ASCII art title
3. **Gathers System Info** - Collects data from system APIs
4. **Formats Output** - Presents data in readable format
5. **Displays Results** - Shows all information with colors

## Dependencies 📦

| Library | Purpose |
|---------|---------|
| `psutil` | System and process utilities |
| `pyfiglet` | ASCII art text generation |
| `termcolor` | Terminal text coloring |
| `platform` | Platform identification |
| `socket` | Network communication |

## Supported Operating Systems 🖥️

- ✅ Windows 10
- ✅ Windows 11
- ✅ Linux
- ✅ macOS
- ✅ Any OS with Python 3.6+

## Use Cases 💡

- **System Diagnostics** - Identify hardware issues
- **Performance Monitoring** - Check resource usage
- **Hardware Inventory** - Document system specifications
- **Network Troubleshooting** - Verify IP and connection
- **IT Administration** - Quick system overview
- **Educational Purpose** - Learn system programming
- **Development** - Monitor system while developing

## Troubleshooting 🔨

### "ModuleNotFoundError: No module named 'psutil'"
```bash
pip install psutil
```

### "ModuleNotFoundError: No module named 'pyfiglet'"
```bash
pip install pyfiglet
```

### "ModuleNotFoundError: No module named 'termcolor'"
```bash
pip install termcolor
```

### Script shows "No connection"
- Check your internet connection
- Firewall might be blocking
- Try with sudo on Linux

### Limited information on some fields
- Some data requires elevated privileges
- Run with `sudo` or administrator mode
- Some features OS-specific

## Performance 🚀

- **Execution Time**: ~1-2 seconds
- **Memory Usage**: Minimal (~10-20MB)
- **CPU Usage**: Negligible
- **Real-time**: Shows current system state

## Limitations ⚠️

- Requires network connection for IP detection
- Some hardware info may need admin/sudo privileges
- Windows version detection limited to Windows 10/11
- Battery info only on laptops with battery sensors

## Future Enhancements 🔮

- GPU information display
- Process monitoring
- Temperature sensors
- USB device detection
- Printer/peripheral detection
- Network speed tests
- Historical data logging

## Author 👨‍💻

Created by **good123453**

## Credits 🙏

- **psutil** - https://github.com/giampaolo/psutil
- **pyfiglet** - https://github.com/pwaller/pyfiglet
- **termcolor** - https://github.com/termcolor/termcolor
- **Python Community** - For amazing libraries

## License 📄

MIT License - See LICENSE file for details

## Contributing 🤝

Found a bug? Have improvements? Feel free to:
- Open an issue
- Submit pull requests
- Share suggestions

## Support 💬

For issues or questions:
- Open a GitHub issue
- Check existing issues first
- Provide system details when reporting bugs

## Disclaimer ⚖️

This tool is provided "as-is" for informational purposes. Use it to:
- ✅ Monitor your own system
- ✅ Learn system programming
- ✅ Troubleshoot issues
- ✅ Educational purposes

---

**Made with ❤️ for system enthusiasts!**

**Happy analyzing! 🎉**
