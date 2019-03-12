**sync ntp**
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



**apt remove**
```bash
####################################################################
##      MYSQL remove
####################################################################

sudo service mysql stop
sudo apt-get remove --purge mysql-server mysql-client mysql-common
sudo apt-get autoremove
sudo apt-get autoclean
sudo rm -rf /var/lib/mysql
sudo rm -rf /etc/mysql


####################################################################
##      MYSQL install
####################################################################
sudo apt-get install mysql-client mysql-server
sudo service mysql stop
```


