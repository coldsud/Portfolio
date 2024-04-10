Bravo Team:
Base64 encoded      = QnJhdm8=


### Decrypt Hexadecimal

this command works great

`echo 4e 65 76 65 72 20 67 6f 6e 6e 61 20 72 75 6e 20 61 72 6f 75 6e 64 20 61 6e 64 20 64 65 73 65 72 74 20 79 6f 75 0a 4e 65 76 65 72 20 67 6f 6e 6e 61 20 6d 61 6b 65 20 79 6f 75 20 63 72 79 0a | xxd -r -p`



Hexdump             = 4e 65 76 65 72 20 67 6f 6e 6e 61 20 72 75 6e 20 61 72 6f 75 6e 64 20 61 6e 64 20 64 65 73 65 72 74 20 79 6f 75 0a 4e 65 76 65 72 20 67 6f 6e 6e 61 20 6d 61 6b 65 20 79 6f 75 20 63 72 79 0a


### Sha1 decode with Hashcat

`hashcat -m100 -a 0 cracksha1.txt /usr/share/seclists/Passwords/cirt-default-passwords.txt`

Hash type (sha1)    = 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8:password
    
    stored in this locationg (~/.local/share/hashcat/hashcat.potfile)


### Unknown Hash attempt
saved hash to text file _unknownhash.txt_
used this command for the potential hashes it could be 

hash-identifier 
Possible Hashs:
[+] SHA-1
[+] MySQL5 - SHA-1(SHA-1($pass))

Command that worked
* `hashcat  -m100 -a 0 unkownhash.txt /usr/share/wordlists/rockyou.txt`




Unknown hash type   = 035EC07A85BB3F2D1262B3245642D13FD606626D::1loveu 