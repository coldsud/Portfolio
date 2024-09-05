```bash
nikto -ask=no -Tuning=x4567890ac -nointeractive -host http://10.10.189.128:80 2>&1 | tee "/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nikto.txt"
```

[/home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nikto.txt](file:///home/kali/Documents/Portfolio/AutoRecon/easyCTF/results/10.10.189.128/scans/tcp80/tcp_80_http_nikto.txt):

```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.189.128
+ Target Hostname:    10.10.189.128
+ Target Port:        80
+ Start Time:         2024-04-17 13:19:28 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /robots.txt: contains 2 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ /: Server may leak inodes via ETags, header found with file /, inode: 2c39, size: 590523e6dfcd7, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: POST, OPTIONS, GET, HEAD .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 7703 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2024-04-17 13:32:07 (GMT-4) (759 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```
