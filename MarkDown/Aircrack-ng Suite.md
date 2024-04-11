### Aircrack-ng Suite

The Aircrack-ng suite of tools is built for assessing the network security of wireless networks. It has tools for monitoring, attacking, testing, and cracking wifi communications. All of the tools in the suite are command line tools, which allows for their use in scripts. Many other programs that use the suite take advantage of this fact. The suite primarily runs on Linux, but technically can run on most operating systems, though running on Windows has very little support.

The tools in the aircrack-ng suite are stored in a couple different directories on Kali. Tools stored in */usr/sbin generally require you to be root user in order to run.
* `ls -l /usr/sbin/air*`

The following three tools are most commonly used to capture and manipulate Wi-Fi traffic:

    airmon-ng - enables and disables monitor mode on a wireless interface.
    airodump-ng - provides the ability to capture 802.11 frames.
    aireplay-ng - injects frames to perform an attack to obtain the authentication credentials for an access point.


* `ls -l /usr/bin/air*`

The aircrack-ng tools found in the /usr/bin can generally be run by any user. They are used to decode frames recovered via airmon-ng and airdump-ng:

    aircrack-ng - attempts to recover the passphrase from a packet capture via an offline dictionary attack.
    airdecap-ng - decrypt captured frames once the passphrase has been recovered.

To find out more about the options and usage of an individual tool within the suite, simply add either --help or -h to the end of the tool name for help.

    Some commands only take --help and others only -h, but it should be noted that usually just typing the name of the command by itself will also show the help and usage information.


### Setting up Aircrack-ng

Before using aircrack-ng in the real world:

    Ensure the wireless adapter is supported and compatible.
    Identify the manufacturer of the wireless card and the chipset manufacturer.

Determining the correct chipset of your wireless card can be a challenge. You have a number of options:

    Search the Internet for the card model to find the chipset.
    Search the forums at the official aircrack-ng website at: https://forum.aircrack-ng.org/
    If the card is working on your Windows system, you may be able to determine the chipset by looking at the Windows driver filenames.
    Check the card manufacturer's website.
    If the card is working on a Linux system, you may be able to use either of the lsusb -vv or lspci -vv commands.
    Locate the FCC ID of your device and search https://www.fcc.gov/oet/ea/fccid for your card.

Next, identify the driver needed for the card. There are different drivers available.

To work with the aircrack-ng suite you must be able to put the wireless card in what is called monitor mode.

    You can find more information and an example of the monitor mode process at: https://www.aircrack-ng.org/doku.php?id=compatibility_drivers

    If you are planning to purchase a card to work with the aircrack-ng suite, see: https://www.aircrack-ng.org/doku.php?id=faq#what_is_the_best_wireless_card_to_buy

To ensure that the card chipset can operate in monitor mode and set up the appropriate driver, use the airmon-ng tool and its options. 

`Airmon-ng` returns an error and does not display any info as we do not have a virtual wireless card in the environment. However, there are certain processes which can also interfere with airmon-ng, so there is an option to test for this.

Type:
* `airmon-ng check` 

Airmon-ng notes one process which could cause problems and indicates that to kill this process you would type airmon-ng check kill,

use the following command to put the wireless card in monitor mode to work with other parts of the suite.
* `airmon-ng start <your wirelesscard interface> 6`

To later disable monitor mode and return the card to managed mode, use the following command:
* `airmon-ng stop <your wirelesscard interface>mon`



        Note the name of the monitoring interface is the default interface name with mon appended to the end, the name used to stop monitoring mode.

Once you have a compatible card and driver, you can place your card in monitor mode and work with other tools in the aircrack-ng suite.

### Using Aircrack-ng Tools

Let's take a look at other aircrack-ng suite tools. We will use the wireless traffic sample capture files from aircrack-ng and the suite of tools to analyze and crack the capture files.

airodump-ng can capture wireless network traffic passwords and usernames. We will use this tool to attempt to crack wifi passwords.

captures files can be opened by programs such as tcpdump and Wireshark, but we will use air-crack-ng to see if we can crack the wifi password.

we'll use this command:
* `aircrack-ng -w password.lst <capture.cap>`