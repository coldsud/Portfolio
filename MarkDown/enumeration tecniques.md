### Enumerating Hosts

During the information gathering phase you will move from passive reconnaissance to active reconnaissance. Here we use the information we gathered to determine our attack vector by starting at the top of the list working our way down. That means retrieving a list of open ports, vulnerable services running on those ports, web directories, or the type of information that can be exposed by the service such as a list of users.

When enumerating a host, we will determine the best possible entry point. Which means you will be going over your scans in detail line by line to find the lowest hanging fruit. 

#### Run a nmap scan to identify hosts on our network.

`nmap -O 10.1.16.0/24 -oX enum.xml && xsltproc enum.xml -o enum.html`

    We are using the -O option to detect the Operating Systems of the hosts on our network.

#### Open enum.html in our firefox browser to view our scan report.

`firefox enum.html`

### Enumerating Ports

We will be determining what versions of the services that are running on our host we previously scanned to identify potential exploits. Our result from our last scan shows us that the host 10.1.16.9 has **_more_** open ports than any other host on the network.

Run another nmap scan to determine the versions of the services on all 65,535 ports open on this machine. Then you will output the scan into an .xml file using the -oX option to create a detailed list.

`nmap -sV -p- 10.1.16.9 -oX enum2.xml`

Convert your .xml file to .html using xsltproc

`xsltproc enum2.xml -o enum2.html`

Open enum2.html in our firefox browser to view our scan report.

`firefox enum2.html`

#### what to do on ports

Run a vulnerability script scan on port 21.

nmap --script=vuln 10.1.16.9 -p 21

### Enumerating Web Directories


There are many tools we can use to enumerate web directories; in this section we will be using Dirb and Nikto to scan our web server.

Dirb is a web content scanner that launches a dictionary-based attack to identify web directories using a dictionary file.

    You can view the web directory files that can be used by dirb by navigating to /usr/share/wordlists/dirb/.

    Type dirb, then press ENTER in your terminal window to see a list of options and command usage examples.


        After typing dirb Scroll up and down in your terminal to see all of the options.

    Using dirb, run a scan on the metasploitable web server.

    dirb http://10.1.16.9/


        You can scroll up and down in the terminal to view the entire output of our scan. When an accessible directory is found it will be noted with ==>

    Our output dirb identified 41,526 files and 89 directories. We can view a directory by typing the webservers directory in the address bar of our browser.

    Open your firefox browser in the top left-hand corner. 

    In the address bar, navigate to the second directory discovered by dirb.

    http://10.1.16.9/dvwa/


    Nikto is a web server vulnerability scanning tool. Nikto will return any cookies received from the web server while attempting to detect files, software, and directories running on the web server.

    Type nikto, then press ENTER in your terminal window to see a list of options and command usage examples.


    In your terminal run a Nikto scan on the metasploitable2 host.

    nikto -h 10.1.16.9


        When a directory is identified our output will show Directory indexing found. or directory found to the right of the directory discovered.

    Nikto discovered numerous directories and even vulnerabilities on this web server. You can navigate to each directory using your web browser.
        /doc/
        /test/
        /icons/
        /phpMyAdmin/

    Example