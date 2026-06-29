# UDP Sound Stream Over LAN - GUI
### do you need to stream your PC sound to another PC on LAN ?
<b>then this project is for you .<b>


A lightweight, cross-platform application for streaming your PC's audio output to another PC on the same local area network with a clean, simple UI, low latency, and an intuitive user experience.

## Supported Platforms

- **Windows 10** (AMD64) ✅ TESTED
- **Windows 11** (AMD64) ✅ TESTED
- **Linux** (AMD64)      ✅ TESTED

- **macOS** ! Not Tested but should work if you can run it from source

## Getting Started

### Windows (AMD64)

Simply download the `.exe` file from [Releases](../../releases) and run it.

### Linux
#
*note: make sure you have python3-tkinter & python3-pyaudio installed on your machine ;
if they are not installed you should install them with your package manager e.g on debian:
sudo apt install python3-tkinter python3-pyaudio
#
1. Clone the repository:
   ```bash
   git clone https://github.com/spiritofthenight/UDP-sound-stream-over-LAN-GUI.git
   cd UDP-sound-stream-over-LAN-GUI
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Build the application for the server:
   ```bash
   pyinstaller guiserver.py --onefile --noconsole --icon icon.ico
   cd dist
   ./guiserver
   ```

5. Repeat the same process for the client:
   ```bash
   pyinstaller guiclient.py --onefile --noconsole --icon icon.ico
   cd dist
   ./guiclient
   ```

## Alternative CLI Version

If you prefer a simpler command-line interface, check out the original CLI version:

[UDP-sound-stream-over-LAN](https://github.com/spiritofthenight/UDP-sound-stream-over-LAN)

## Notes

- This application was developed and tested with **Python 3.12**
- If you encounter issues with NumPy version 1.26.4, you can use **NumPy 2.4.6** with Python 3.13.5 as an alternative
