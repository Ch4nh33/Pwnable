from pwn import*

p = process('./a.out')
data = p.recv(13)
print(data)

p.interactive()
