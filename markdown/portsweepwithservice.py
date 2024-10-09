import sys
import socket
import multiprocessing

# Function to scan ports
def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout of 1 second
        result = s.connect_ex((target, port))
        if result == 0:
            service = socket.getservbyport(port)
            print("Port {} ({}) is open".format(port, service))
        s.close()
    except KeyboardInterrupt:
        print("\n Exiting")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved")
        sys.exit()
    except socket.error:
        print("\n Server not responding")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        target = input("Enter target IP address or hostname: ")

    # Create multiprocessing pool
    pool = multiprocessing.Pool()

    # Scan ports using multiprocessing pool
    results = []
    for port in range(1, 65536):  # Scan ports from 1 to 65535
        results.append(pool.apply_async(scan_port, args=(target, port)))

    # Close the pool and wait for all processes to complete
    pool.close()
    pool.join()

    # Get results from the multiprocessing pool
    for result in results:
        result.get()
