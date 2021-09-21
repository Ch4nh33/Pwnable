#load 
from pwn import*

#local connection
p = process('./a.out')

#server connection
p = remote('server address',number)

