from pwn import*

p = process('./a.out')
p.sendline('AAA')
p.interactive()
