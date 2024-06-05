import socket
import threading

# Function to scan a single IP address
def scan_ip(ip):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        # Try to connect to the IP address on port 80
        s.connect((ip, 80))

        # If connection is successful, print the IP address
        print(f"Active IP: {ip}")

        # Close the socket
        s.close()
    except:
        pass

# Main function to scan a range of IP addresses
def main():
    # Define the IP range to scan
    ip_prefix = "192.168.1."
    start_ip = 1
    end_ip = 254

    # Create a thread for each IP address in the range
    threads = []
    for ip_suffix in range(start_ip, end_ip + 1):
        ip = ip_prefix + str(ip_suffix)
        thread = threading.Thread(target=scan_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
