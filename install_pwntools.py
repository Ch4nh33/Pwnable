#load 
from pwn import*

#local connection
p = process('./a.out')

#server connection
p = remote('ctf.j09nhyun.xyz',3000)

