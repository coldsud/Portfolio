Here’s the guide in a Markdown-friendly format, crafted to maintain its structure and readability when pasted into VS Code.

---

# Comprehensive Setup Guide: Docker, Wyze-Bridge, and WireGuard VPN on Ubuntu

This guide provides step-by-step instructions for setting up Docker, installing Wyze-Bridge for video streaming, and configuring WireGuard VPN for secure remote access. Each section is methodically designed to ensure the server is fully operational and secure.

---

## Table of Contents
1. [Install Docker on Ubuntu](#install-docker-on-ubuntu)
2. [Install Wyze-Bridge Using Docker](#install-wyze-bridge-using-docker)
3. [Install and Configure WireGuard for VPN Access](#install-and-configure-wireguard-for-vpn-access)

---

## 1. Install Docker on Ubuntu

Docker is essential for running Wyze-Bridge in a contained environment.

### Step-by-Step Instructions

1. **Update Package Lists**:
   ```bash
   sudo apt update
   ```

2. **Install Dependencies**:
   ```bash
   sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
   ```

3. **Add Docker’s GPG Key**:
   ```bash
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   ```

4. **Add Docker Repository**:
   ```bash
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```

5. **Install Docker**:
   ```bash
   sudo apt update
   sudo apt install docker-ce -y
   ```

6. **Start and Enable Docker**:
   ```bash
   sudo systemctl enable docker
   sudo systemctl start docker
   ```

7. **Verify Docker Installation**:
   ```bash
   docker --version
   ```

---

## 2. Install Wyze-Bridge Using Docker

Wyze-Bridge enables streaming from Wyze cameras. We’ll use Docker to run it.

### Step-by-Step Instructions

1. **Create a Directory for Wyze-Bridge**:
   ```bash
   mkdir ~/wyze-bridge && cd ~/wyze-bridge
   ```

2. **Create a `docker-compose.yml` File**:
   ```bash
   nano docker-compose.yml
   ```

3. **Add Wyze-Bridge Configuration**:
   Copy and paste the following, replacing `YOUR_WYZE_EMAIL` and `YOUR_WYZE_PASSWORD` with your Wyze account credentials.

   ```yaml
   version: '3'
   services:
     wyze-bridge:
       image: mrlt8/wyze-bridge:latest
       container_name: wyze-bridge
       environment:
         - WYZE_EMAIL=YOUR_WYZE_EMAIL
         - WYZE_PASSWORD=YOUR_WYZE_PASSWORD
       ports:
         - 8554:8554    # RTSP stream port
         - 8888:8888    # WebRTC stream port
         - 5000:5000    # Web UI port
       restart: unless-stopped
   ```

4. **Start Wyze-Bridge**:
   ```bash
   sudo docker-compose up -d
   ```

5. **Check if Wyze-Bridge is Running**:
   ```bash
   sudo docker ps
   ```

6. **Access Wyze-Bridge Web Interface**:
   - Go to `http://YOUR_SERVER_IP:5000` to access the Wyze-Bridge Web UI.

---

## 3. Install and Configure WireGuard for VPN Access

WireGuard provides secure remote access to your server, allowing you to connect safely from anywhere.

### Generate Server Keys and Configure WireGuard

1. **Install WireGuard**:
   ```bash
   sudo apt install wireguard -y
   ```

2. **Create a Directory for WireGuard Configuration**:
   ```bash
   sudo mkdir -p /etc/wireguard
   ```

3. **Generate Server Private and Public Keys**:
   - **Private Key**:
     ```bash
     sudo wg genkey | sudo tee /etc/wireguard/server_private.key
     ```
   - **Public Key**:
     ```bash
     sudo cat /etc/wireguard/server_private.key | wg pubkey | sudo tee /etc/wireguard/server_public.key
     ```

   **Note**: Keep these keys secure.

### Configure WireGuard Server

1. **Create Server Configuration File**:
   ```bash
   sudo nano /etc/wireguard/wg0.conf
   ```

2. **Add Server Configuration**:
   Replace `YOUR_SERVER_PRIVATE_KEY` and `YOUR_NETWORK_INTERFACE` as necessary.

   ```ini
   [Interface]
   PrivateKey = YOUR_SERVER_PRIVATE_KEY
   Address = 10.8.0.1/24
   ListenPort = 51820

   # IP forwarding and NAT
   PostUp = iptables -t nat -A POSTROUTING -o YOUR_NETWORK_INTERFACE -j MASQUERADE; sysctl -w net.ipv4.ip_forward=1
   PostDown = iptables -t nat -D POSTROUTING -o YOUR_NETWORK_INTERFACE -j MASQUERADE; sysctl -w net.ipv4.ip_forward=0
   ```

3. **Enable IP Forwarding**:
   ```bash
   sudo sysctl -w net.ipv4.ip_forward=1
   echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
   ```

4. **Start and Enable WireGuard Service**:
   ```bash
   sudo wg-quick up wg0
   sudo systemctl enable wg-quick@wg0
   ```

---

### Configure WireGuard Client (e.g., Phone)

1. **Generate Client Keys**:
   ```bash
   wg genkey | sudo tee /etc/wireguard/client_private.key | wg pubkey | sudo tee /etc/wireguard/client_public.key
   ```

2. **Add Client as Peer in Server Configuration**:
   Edit the `wg0.conf` file to add the client as a peer.

   ```ini
   [Peer]
   PublicKey = YOUR_CLIENT_PUBLIC_KEY
   AllowedIPs = 10.8.0.2/32
   ```

3. **Restart WireGuard**:
   ```bash
   sudo wg-quick down wg0
   sudo wg-quick up wg0
   ```

### Create Client Configuration File

1. **Create Client Configuration File**:
   ```bash
   sudo nano /etc/wireguard/client.conf
   ```

2. **Add Client Configuration**:
   Replace placeholders as necessary.

   ```ini
   [Interface]
   PrivateKey = YOUR_CLIENT_PRIVATE_KEY
   Address = 10.8.0.2/24
   DNS = 8.8.8.8

   [Peer]
   PublicKey = YOUR_SERVER_PUBLIC_KEY
   Endpoint = YOUR_SERVER_IP:51820
   AllowedIPs = 0.0.0.0/0
   PersistentKeepalive = 21
   ```

3. **Transfer Client Configuration to Phone**.

4. **Connect to VPN**: Open WireGuard on your phone and import the client configuration file.

---

### Secure VPN Access to Wyze-Bridge

1. **Access Wyze-Bridge through VPN**: 
   - Once connected, go to `http://10.8.0.1:5000` to access the Wyze-Bridge interface.

2. **Tighten IP Restrictions** (Optional):
   In `wg0.conf`, restrict access to necessary IPs.

   ```ini
   [Peer]
   PublicKey = YOUR_CLIENT_PUBLIC_KEY
   AllowedIPs = 10.8.0.1/32, 10.0.0.251/32
   ```

3. **Apply Changes**:
   ```bash
   sudo wg-quick down wg0
   sudo wg-quick up wg0
   ```

This guide covers the setup of Docker, Wyze-Bridge, and WireGuard, with VPN access for secure remote video streaming on Ubuntu. Following these steps, you’ll have a secure and replicable setup.