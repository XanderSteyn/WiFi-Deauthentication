---

# 🚨 Deauth Packet Sender

A Python-based tool that sends deauthentication (Deauth) packets to disconnect a target device from a Wi-Fi network using Scapy.

⚠️ **Use responsibly** – Only run this tool on networks you own or have explicit permission to test.

## ⚙️ Features
- Sends deauthentication packets to disconnect a target device from a Wi-Fi network.
- Uses Scapy to craft and send packets over the air.
- Simple and easy-to-use command-line interface.

## 🚀 Installation

### Prerequisites

To run this project, you'll need Python 3.x installed and the following dependencies :

```bash
pip install scapy
```

### 🛠️ Setup

1. Clone the repository to your local machine :

   ```bash
   git clone https://github.com/XanderSteyn/WiFi-Deauthentication.git
   cd WiFi-Deauthentication
   ```

2. Ensure that you're running the script with administrator privileges or using a privileged account (e.g. `sudo` in Linux).

3. Run the script:

   ```bash
   python WiFiDeauth.py
   ```

### 📦 Dependencies

- `scapy` A powerful Python library used to interact with and manipulate network packets.

## 🛑 How It Works

- The script takes the target device's MAC address, the gateway/router's MAC address, and your Wi-Fi interface (e.g. `wlan0` on Linux).
- It then crafts a deauthentication packet and sends it continuously in a loop to disconnect the target device from the network.
- This is useful for testing and educational purposes, but please make sure to follow ethical guidelines when using it.

## 📝 Usage

1. Run the script :
   ```bash
   python WiFiDeauth.py
   ```

2. Provide the following inputs :
   - **Target MAC Address** : The MAC address of the device you want to disconnect from the network.
   - **Gateway MAC Address** : The MAC address of the router or access point.
   - **Wi-Fi Interface** : The network interface on your system (e.g., `wlan0` on Linux).

3. The script will start sending deauthentication packets to the target device.

## ⚙️ Configuration

- **Packet Count** : The script sends 100 deauthentication packets in each iteration with a delay of 0.1 seconds between them. You can modify the `count` and `inter` values to adjust the packet sending rate.

---
