#! bin/python

import socket
import datetime
import sys

if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1])

print("-" * 50)
print("Scanning target "+ target)
print("Time started" + str(datetime.now())
try:
    for port in range(50,85);
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target_port))
    if result == 0:
        print(f"Port {} is open", format(port))
    s.close

except KeyboardInterrupt:
    print("\n Exiting program")
    sys.exit()
except socket.gaierror;
    print("Hostname not resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()



