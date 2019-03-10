** sync ntp **
```bash
[root]# ntpdate -q time.bora.net


[root]# cat /etc/ntp.conf
server 10.40.83.251 iburst
[root@]# service ntpd start
Redirecting to /bin/systemctl start ntpd.service
[root]# ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 10.40.83.251    .INIT.          16 u    -   64    0    0.000    0.000   0.000
[root]#

```
