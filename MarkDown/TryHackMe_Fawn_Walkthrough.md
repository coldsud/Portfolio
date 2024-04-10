### TryHackMe_Fawn_Walkthrough
This how I solved Fawn. First thing was to connect to the network with openvpn. You'll download the openvp configuration file from the HTB (HackTheBox) website.

Once you are connected: Spawn the machine. This will give you the IP to work with  
Force this case the machine IP was: `10.129.158.92`

#### Recon
I first ran a nmap scan to discover OS and ports with services by utilizing this command.
* `sudo nmap -sV -O 10.129.158.92 -oX enum.xml`
    * `-oX enum.xml` outputs the results into an xml file for which I convert to html to read the results better.
    
    To convert .xml to .html: `xsltproc enum.xml -o enum.html`

Next i'm going to run a vulnerability script on port 21 since it is open
* `sudo nmap -p 21 --script=vuln 10.129.158.92`
    * There is an exploit found 
                
        [CVE-2011-1002](https://nvd.nist.gov/vuln/detail/CVE-2011-1002)

Next we'll go to nvd.gov to find more about this vulnerability.

However, we have found that port 21 with the ftp service to be open so, we may want to look for an easier infiltration vector. There could be default creds still available to login with.

Let's install FTP by running this command
* `sudo apt install ftp`

then we simply run this command to connect to the ftp service:

* `ftp 10.129.158.92`

We can easily search for default ftp creds online. with search engines such as google or bing.