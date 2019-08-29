**setup key based ssh on CentOS-7**
```bash
===================================================================
1. Server Side
===================================================================
A. key generate
  - Private Key : id_rsa      -> Move Client
  - Public Key  : id_rsa.pub  -> Keep Local Server

$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/suser/.ssh/id_rsa):
/home/suser/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):               [+] Empty means no password when connection.
Enter same passphrase again:
Your identification has been saved in /home/suser/.ssh/id_rsa.
Your public key has been saved in /home/suser/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:/BcPAC8+jOyhnnuvjgpue7Nps91qSL348yg0C5RBk7A suser@mojave
The key's randomart image is:
+---[RSA 2048]----+
|+o.     .        |
| +.      o       |
|E o     . o      |
| o   . = . .     |
|.   . + S   o    |
| . + + . o   +   |
|. + * o   . . .  |
|.o @o*+    .     |
|.o==&O*=.        |
+----[SHA256]-----+

B. Keep Public Key on Local Server
$ cat id_rsa.pub > authorized_keys

===================================================================
2. Client Side
===================================================================
A. Try connect using Private Key(id_rsa)
$ ssh -i id_rsa suser@localhost
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:PVvcQ3vvx5UayS2j/P0mhQ9xog4yCuoTIx/WknyirtI.
ECDSA key fingerprint is MD5:55:bc:35:15:35:6e:45:b2:e9:59:c3:de:25:6c:48:41.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'localhost' (ECDSA) to the list of known hosts.

Last login: Thu Aug 29 15:25:30 2019 from localhost
$ ps
  PID TTY          TIME CMD
28949 pts/1    00:00:00 bash
28987 pts/1    00:00:00 ps
$ logout
Connection to localhost closed.
$


===================================================================
3. Use Case putty on Windows
===================================================================
A. Convert Private Key to ppk format
 - Putty Key Generate
 - Load (id_rsa)
 - Save private key : save ppk format [+] Empty password means no password when connection.
 
B. Try connect using Private Key(id_rsa.ppk)
  - Putty > Connection > SSH > Auth > Private key file
  
login as: suser

Authenticating with public key "imported-openssh-key"
Last login: Thu Aug 29 15:26:37 2019 from localhost
$ id
uid=1000(suser) gid=1000(suser) groups=1000(suser),10(wheel) context=unconfined_                                             u:unconfined_r:unconfined_t:s0-s0:c0.c1023
$

```
