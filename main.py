import psutil
from datetime import datetime

SUSPICIOUS_IPS = ["51.116.253.169","140.82.114.26","192.168.1.117","198.51.100.1","198.51.100.2","144.2.15.21","23.212.253.202",]

def check_estabilished_connections():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Scanning established connections...")
    print(f"{'PID':<8} {'Process Name':<20} {'Local Address':<22} {'Remote Address':<22} {'Status'}")
    print("-" * 85)

    #suspicious ip chack
    suspicious_pound =[]

    for conn in psutil.net_connections(kind='inet'):
        if conn.status == "ESTABLISHED" and conn.raddr:
            remote_ip = conn.raddr.ip
            remote_port = conn.raddr.port
            local_ip = conn.laddr.ip
            local_port = conn.laddr.port

            try:
                process = psutil.Process(conn.pid)
                process_name = process.name()

            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                process_name = "unknown/protected"

            local_address = f"{local_ip}:{local_port}"
            remote_address = f"{remote_ip}:{remote_port}"

            print(f"{str(conn.pid):<8} {process_name:<20} {local_address:<22} {remote_address:<22} {conn.status}")

            #remot ip search
            if remote_ip in SUSPICIOUS_IPS:
                suspicious_pound.append({
                    "pid": conn.pid,
                    'name':process_name,
                    "remote": remote_address
                })

    print("_" * 80)
    return suspicious_pound

def main():

    #alearts message to use
    alerts = check_estabilished_connections()
    if alerts:
        print(f"\n[ALERT] Found {len(alerts)} suspicious connections")
        for alert in alerts:
            print(f" -> CRITICAL: Process '{alert['name']}' (PID: {alert['pid']}) is connected to suspicious IP: {alert['remote']}")
    else:
        print("\n No suspicious connections detected.")


if __name__ == "__main__":
    main()
