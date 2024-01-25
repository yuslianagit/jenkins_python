import psutil

import requests
 
class SystemMonitor:

    @staticmethod

    def check_disk_usage():

        disk_usage = psutil.disk_usage('/')

        return disk_usage.percent > 20
 
    @staticmethod

    def check_cpu_utilization():

        cpu_utilization = psutil.cpu_percent()

        return cpu_utilization < 75
 
    @staticmethod

    def check_localhost_availability():

        try:

            socket_info = psutil.net_if_addrs()

            return 'lo' in socket_info

        except Exception as e:

            print(f"Error checking localhost availability: {e}")

            return False
 
    @staticmethod

    def check_internet_availability():

        try:

            response = requests.get("http://www.google.com", timeout=5)

            return response.status_code == 200

        except requests.ConnectionError:

            return False
 
def main():

    monitor = SystemMonitor()
 
    disk_status = monitor.check_disk_usage()

    cpu_status = monitor.check_cpu_utilization()

    localhost_status = monitor.check_localhost_availability()

    internet_status = monitor.check_internet_availability()
 
    if not disk_status or not cpu_status:

        print("ERROR! Disk usage or CPU utilization exceeded thresholds.")

    elif localhost_status and internet_status:

        print("Everything is OK.")

    else:

        print("Network checks failed.")
 
if __name__ == "__main__":

    main()
