```bash
nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.189.128
```

[/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nmap.txt](file:///home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nmap.txt):

```
# Nmap 7.94SVN scan initiated Wed Apr 17 13:19:15 2024 as: nmap -vv --reason -Pn -T4 -sV -p 80 "--script=banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN /home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nmap.txt -oX /home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/xml/tcp_80_http_nmap.xml 10.10.189.128
Nmap scan report for 10.10.189.128
Host is up, received user-set.
Scanned at 2024-04-17 13:19:15 EDT for 1s

PORT   STATE    SERVICE REASON      VERSION
80/tcp filtered http    no-response

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Wed Apr 17 13:19:16 2024 -- 1 IP address (1 host up) scanned in 1.51 seconds

```
