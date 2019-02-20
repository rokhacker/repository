***NMAP Options***


```bash
[root@linuxserver ~]# time nmap -PN -O -sV -sT -T3 -p 1-65535 127.0.0.1
Starting Nmap 7.70 ( https://nmap.org ) at 2019-02-20 16:59 KST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000056s latency).
Not shown: 65530 closed ports
PORT      STATE SERVICE       VERSION
22/tcp    open  ssh           OpenSSH 7.4 (protocol 2.0)
3306/tcp  open  mysql         MySQL 5.5.5-10.1.36-MariaDB
3350/tcp  open  findviatv?
3389/tcp  open  ms-wbt-server xrdp
17123/tcp open  http          Tornado httpd 4.3
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.8 - 4.14
Network Distance: 0 hops

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.81 seconds

real    0m29.861s
user    0m2.019s
sys     0m1.746s
[root@linuxserver ~]#
```


| Option | Description |
|:--------:|:--------|
|**-PN**| do not ping scan |
|**-O** | Enable OS detection |
|**-A** |  Enable OS detection, version detection, script scanning, and traceroute |
|**-sV** | Probe open ports to determine service/version info |
|**-sT** | do Connect() scan |
|**-T<0-5>** | Set timing template (higher is faster) |
|**-p <port ranges>** | Only scan specified ports |
|**-v** | Increase verbosity level (use -vv or more for greater effect) |
