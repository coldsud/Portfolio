## HTB Crocodile Walkthrough

### Recon

Spawned Targed ID
10.129.184.140

Run a nmap scan against target 
* `sudo nmap -sV -O 10.129.184.140`

### Task 1

What Nmap scanning switch employs the use of default scripts during a scan?

    -sC

#### Scan results

Not shown: 997 closed tcp ports (reset)
PORT      STATE      SERVICE VERSION
21/tcp    open       ftp     vsftpd 3.0.3
53/tcp    filtered   domain
80/tcp    open       http    Apache httpd 2.4.41 ((Ubuntu))



### Task 2

What service version is found to be running on port 21?

     vsftpd 3.0.3

To login to the FTP server:
Anonymous Login is enabled type this command to ftp into 10.129.184.140
* `ftp 10.129.184.140`   
Then login in with:
* `anonymous`


### Task 3

What FTP code is returned to us for the "Anonymous FTP login allowed" message?

            230

### Task 4

After connecting to the FTP server using the ftp client, what username do we provide when prompted to log in anonymously? 

            anonymous

### Task 5

After connecting to the FTP server anonymously, what command can we use to download the files we find on the FTP server? 

            get

After FTP login into server 10.129.184.140
run command to show directories
* `ls`

you will see two directories, which we download.

            allowed.userlist
            allowed.userlist.passwd

be aware of where you are were you are downloading these files and run the get command to retrieve file:
* `get allowed.userlist`
* `get allowed.userlist.passwd`

### Task 6

What is one of the higher-privilege sounding usernames in 'allowed.userlist' that we download from the FTP server? 

            admin

### Task 7

What version of Apache HTTP Server is running on the target host? (refer to previous nmap scan results helpful switch -sV)

           Apache httpd 2.4.41 

###  Task 8

What switch can we use with Gobuster to specify we are looking for specific filetypes? 

            -x

###  Task 9

Which PHP file can we identify with directory brute force that will provide the opportunity to authenticate to the web service? 

For this task we need to run `gobuster` or `feroxbuster` to disover some sort of login page. Utilizing `feroxbuster` run this command:
* `feroxbuster -u http://10.129.184.140 --extensions "php.txt"`

this came back with these directories availble for traversal

    http://10.129.184.140/assets/js/vendor/
    http://10.129.184.140/assets/images/portfolio/
    http://10.129.184.140/js/
    http://10.129.184.140/css/
    http://10.129.184.140/assets/js/
    http://10.129.184.140/assets/images/slider/
    http://10.129.184.140/assets/
    http://10.129.184.140/assets/css/
    http://10.129.184.140/assets/images/
    http://10.129.184.140/assets/fonts/
    http://10.129.184.140/fonts/
    http://10.129.184.140/dashboard/ 

for this we will select the _dashboard_ directory in hopes for a login page. which it did redirect "login.php

the answer for **Task 9** is:

        login.php


from here we will login using the credentials harvested from the FTP server files we download.

        username: admin
          passwd: rKXM59ESxesUFHAd

once logged in you'll see the **root flag** on the page

    c7110277ac44d78b6a9fff2232434d16
