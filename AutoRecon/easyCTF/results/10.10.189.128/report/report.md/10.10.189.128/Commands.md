```bash
nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/_quick_tcp_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/xml/_quick_tcp_nmap.xml" 10.10.189.128

nmap -vv --reason -Pn -T4 -sV -sC --version-all -A --osscan-guess -p- -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/_full_tcp_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/xml/_full_tcp_nmap.xml" 10.10.189.128

nmap -vv --reason -Pn -T4 -sV -p 21 --script="banner,(ftp* or ssl*) and not (brute or broadcast or dos or external or fuzzer)" -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp21/tcp_21_ftp_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp21/xml/tcp_21_ftp_nmap.xml" 10.10.189.128

feroxbuster -u http://10.10.189.128:80/ -t 10 -w /home/kali/.local/share/AutoRecon/wordlists/dirbuster.txt -x "txt,html,php,asp,aspx,jsp" -v -k -n -q -e -r -o "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_feroxbuster_dirbuster.txt"

curl -sSikf http://10.10.189.128:80/.well-known/security.txt

curl -sSikf http://10.10.189.128:80/robots.txt

curl -sSik http://10.10.189.128:80/

nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.189.128:80 2>&1 | tee "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nikto.txt"

nmap -vv --reason -Pn -T4 -sV -p 80 --script="banner,(http* or ssl*) and not (brute or broadcast or dos or external or http-slowloris* or fuzzer)" -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/xml/tcp_80_http_nmap.xml" 10.10.189.128

whatweb --color=never --no-errors -a 3 -v http://10.10.189.128:80 2>&1

wkhtmltoimage --format png http://10.10.189.128:80/ /home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_screenshot.png

nmap -vv --reason -Pn -T4 -sV -p 2222 --script="banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods" -oN "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp2222/tcp_2222_ssh_nmap.txt" -oX "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp2222/xml/tcp_2222_ssh_nmap.xml" 10.10.189.128


```