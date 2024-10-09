### The Metasploit Framework

The Metasploit Framework is a very powerful tool for penetration testing. It is a text-based, menu-driven program that comes in both a Commercial Pro and an open source or Community version. The Community edition is included with Kali and can also be installed on other systems. 

Metasploit can be launched from the Kali menus under the Favorites or Exploitation Tools sub menus or by typing msfconsole at the command line.

`msfconsole`

Metasploit menu

Metasploit comes with hundreds of exploits, payloads and additional resources to assist during a penetration test.

Before diving into the exploits and other resources, let's take a brief tour of the system.

To begin, enter help and scroll up to review all the available options within Metasploit.

Metasploit help

    One command to note is msfupdate. This command is not found in the help menu and will not work in this lab environment, but should be run from time to time on a live installation in order to keep Metasploit up-to-date with the latest exploits and resources.

The Search command is also a powerful tool in Metasploit. You can use it to look for anything within the Metasploit framework. The Search command offers options such as name: and type: to help narrow down your search.

To use search, type search name:Apple type:exploit for potential Apple exploits.

search name:Apple type:exploit

Metasploit search

A number of potential exploits are returned, note:

    Exploits and resources in Metasploit are organized in a folder structure.
    The Rank column rates exploits from: excellent, great, good, normal to average. 

    Generally, one would want to use a higher ranked exploit during a pen test to achieve a higher rate of success. It is also worth noting that many of these exploits are old and thus would only work against older and unpatched systems.

Scroll to the first entry in the Search results, which is an Apple browser exploit, ranked: good.

Let's find out more about this exploit with the command info.

    Info is a powerful command that returns important information about each exploit or module, such as:

        Name
        Platform
        Available targets
        Basic options - required options you will need to know in order to set up and use the exploit.

Type info exploit/apple_ios/browser/safari_libtiff for more info on this exploit.

info exploit/apple_ios/browser/safari_libtiff

Metasploit info

    You can also use Tab completion to finish commands without typing each letter. The info command below could be typed as follows: info ex[tab]ap[tab]br[tab]sa[tab]. Metasploit fully supports tab given the underlying directory structure it uses.

### Using Attack Modules in Metasploit

Metasploit contains hundreds of exploits and attack auxiliary tools available to you with the use command. Next, you are going to attempt to attack the FTP server on the target using the ftp_login auxiliary tool.

    Continuing in the Terminal of the PT1-Kali virtual machine, type use auxiliary/scanner/ftp/ftp_login to perform an ftp login attack.

    use auxiliary/scanner/ftp/ftp_login

    Metasploit use ftp_login

    Type show options to show the available options.

    show options

    Metasploit show options

    There are a number of possible options and most aren't required. You can change the value of an option with the set command.

    How many options of the ftp_login module are required?  (Answer with a number not the word).

Next, you will be using small dictionaries or files of bad usernames and passwords to see if we can gave access to the FTP service. These will be used as options for this scanner.

Go to the Desktop and Double click the Student-Resource CD icon (you may need to minimize the Terminal) and open File Manager. This mounts the CD and makes the files available. Then close File Manager and return to your open Terminal window.

Type set PASS_FILE /media/cdrom0/Lab14/top13-bad-passwords.txt to set the path to the password list you will use.

set PASS_FILE /media/cdrom0/Lab14/top13-bad-passwords.txt

Metasploit set PASS_FILE

Type set USER_FILE /media/cdrom0/Lab14/top13-bad-usernames.txt to set the path to the username list you will use.

set USER_FILE /media/cdrom0/Lab14/top13-bad-usernames.txt

Metasploit set USER_FILE

The USER_FILE and PASS_FILE are lists of usernames and passwords listed one to a line. There is also an option to use a USERPASS_FILE which contains pairs of usernames and passwords listed are one to a line.

Type set RHOSTS 10.1.16.9 to set the IP address of the target.

set RHOSTS 10.1.16.9

Metasploit set RHOSTS

Type show options again to see the available options.

show options

Metasploit show options set

Finally, type run to execute the attack.

run

Metasploit run 1

Metasploit run 2

Metasploit run 3

How many successful logins were found on the FTP server? (Note: Type the number not the word).

Repeat this exercise using at least one of the other scanners mentioned in the knowledge box below. They all work in similar ways as Metasploit modules. You will start with the use command like in step 2 above, then set the options as with this example, then finally run the module.

    In addtion to the ftp_login scanner, Metasploit comes with scanners for SSH, Telnet, SMB, and SMTP.
