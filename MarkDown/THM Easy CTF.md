## THM Easy CTF

### recon
Target IP: `10.10.54.244`

    PORT     STATE SERVICE
    21/tcp   open  ftp
    80/tcp   open  http
    2222/tcp open  EtherNetIP-1 (ssh) SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8 exploit

### Path to root priveldge

ftp into port 21 
    login: anonymous

download: get Formitch.txt

feroxbuster: http port 80

    find login page with php.login


brute force login page with hydra using:
    username: mitch 
    password list: seclists top 100 or more passwords

username: mitch
password: secret


ssh into box on port 2222 with mitch as user
ssh -p 2222 mitch@<ip>
login with password above.

