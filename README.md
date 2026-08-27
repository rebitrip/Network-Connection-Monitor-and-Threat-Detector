
# 🛡️ Network Connection Monitor & and Threat Detector

> A Python-based network security monitoring tool that analyzes established network connections and detects connections to predefined suspicious IP addresses.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Security](https://img.shields.io/badge/Focus-Network%20Security-red)
![SOC](https://img.shields.io/badge/Focus-SOC%20Monitoring-orange)
![psutil](https://img.shields.io/badge/Library-psutil-green)

---

## 📌 Overview

**Network Connection Monitor & Threat Detector** is a lightweight Python security tool designed to monitor active network connections on a system.

The application uses the Python `psutil` library to inspect established Internet connections, identify the associated process, and compare remote IP addresses against a predefined suspicious IP list.

If a connection matches a suspicious IP, the application generates a **CRITICAL alert** containing the process name, PID, and remote address.

---

## ✨ Features

* 🔍 Monitor established network connections
* 🌐 Identify remote IP addresses and ports
* 🖥️ Display the process associated with each connection
* 🆔 Display Process ID (PID)
* 🚨 Detect connections to predefined suspicious IP addresses
* ⚠️ Generate security alerts
* 🕒 Display connection scan timestamps
* 🔐 Handle process access and permission errors
* 💻 Lightweight command-line interface

---

## 🏗️ Architecture

```text
             Operating System
                    │
                    ▼
              psutil Library
                    │
                    ▼
          Network Connections
                    │
                    ▼
          ESTABLISHED Connections
                    │
             ┌──────┴──────┐
             │             │
             ▼             ▼
        Process Info    Remote IP
                           │
                           ▼
                  Suspicious IP List
                           │
                    ┌──────┴──────┐
                    │             │
                    ▼             ▼
                 Match         No Match
                    │             │
                    ▼             ▼
                 ALERT          Normal
```

---

## 📂 Project Structure

```text
network-connection-monitor/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

| File               | Description                              |
| ------------------ | ---------------------------------------- |
| `main.py`          | Main network monitoring application      |
| `requirements.txt` | Python dependency                        |
| `.gitignore`       | Excludes unnecessary and sensitive files |
| `README.md`        | Project documentation                    |

---

## 🛠️ Technologies

* **Python 3**
* **psutil**
* TCP/IP Networking
* Network Security Monitoring
* Command-Line Interface

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/network-connection-monitor.git
```

### 2. Enter the Project Directory

```bash
cd network-connection-monitor
```

### 3. Create a Virtual Environment

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run:

```bash
python main.py
```

Depending on the operating system, administrator/root privileges may be required to view all process-to-connection mappings.

---

## 📊 Example Output

```text
[2026-08-27 18:30:10] Scanning established connections...

PID      Process Name         Local Address          Remote Address         Status
-----------------------------------------------------------------------------------------------
1234     chrome.exe           192.168.1.10:52341     142.250.72.14:443       ESTABLISHED
4567     python.exe           192.168.1.10:52350     198.51.100.2:443        ESTABLISHED
-----------------------------------------------------------------------------------------------

[ALERT] Found 1 suspicious connection(s)

 -> CRITICAL: Process 'python.exe' (PID: 4567) is connected to suspicious IP: 198.51.100.2:443
```

---

## 🔎 Detection Logic

The tool checks only connections where:

```text
Connection Status = ESTABLISHED
```

For each established connection, it extracts:

```text
PID
Process Name
Local IP
Local Port
Remote IP
Remote Port
Connection Status
```

The remote IP is then compared against the configured suspicious IP list.

```text
Remote IP
    │
    ▼
Is IP in suspicious list?
    │
 ┌──┴──┐
 │     │
Yes    No
 │     │
 ▼     ▼
ALERT  Normal
```

---

## 🚨 Alert Information

When a suspicious connection is detected, the tool reports:

* Process name
* Process ID
* Remote IP
* Remote port
* Connection status

Example:

```text
CRITICAL:
Process 'python.exe'
PID: 4567
Remote: 198.51.100.2:443
```

---

## 🧠 Security Use Case

This project demonstrates a basic endpoint network-monitoring capability that can be useful for learning about:

* SOC monitoring
* Network connections
* Suspicious outbound traffic
* Process-to-network correlation
* IOC-based detection
* Endpoint security
* Incident investigation

A suspicious IP match should be treated as an **indicator for investigation**, not automatic proof of malicious activity.

---

## 🔐 Error Handling

The application handles common process-related exceptions:

```python
psutil.NoSuchProcess
psutil.AccessDenied
psutil.ZombieProcess
```

This prevents the monitoring process from terminating when a process disappears or its information cannot be accessed.

---

## 🚀 Future Improvements

Planned improvements include:

* 📡 Real-time continuous monitoring
* 📝 Security event logging
* 📄 Automated incident reports
* 📧 Email alerts
* 🔔 Desktop notifications
* 🌐 IP reputation API integration
* 📊 HTML dashboard
* 📈 Network activity statistics
* 🗄️ SQLite database logging
* 🔍 DNS/domain correlation
* 🚨 Severity classification
* 🔄 Automatic IOC list updates
* 🛡️ Integration with SIEM platforms such as Wazuh

---

## 🎯 Learning Objectives

This project was built to strengthen practical knowledge of:

```text
Python
   │
   ├── Process Management
   ├── Exception Handling
   ├── File/Module Organization
   │
   ▼
Network Monitoring
   │
   ├── TCP/IP Connections
   ├── Ports
   ├── Remote IPs
   └── Process Correlation
   │
   ▼
SOC Concepts
   │
   ├── IOC Detection
   ├── Alert Generation
   └── Security Investigation
```

---

## 👨‍💻 Author

**Joynul Hasan**

Aspiring Security Operations Center (SOC) Analyst

**Focus Areas:**

`Security Monitoring` • `Threat Detection` • `Network Security` • `Python` • `Incident Response`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

> 🛡️ **Built for learning, security monitoring, and SOC skill development.**
