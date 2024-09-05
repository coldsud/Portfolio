### Hashcat Notes

basic hash crack command would look like this

* `hashcat -m100 -a 0 password.txt /usr/share/seclists/Passwords/cirt-default-passwords.txt`

The above command is example of trying to crack a password in password.txt by chacking it against the cirt-default-passwords.txt

if you are do crack the password it will write to a file call **_hashcat.potfile_** located in here:

    ~/.local/share/hashcat/hashcat.potfile