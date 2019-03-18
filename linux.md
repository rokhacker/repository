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



**apt remove on ubuntu**
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



**setting iptables on centos 7**
```bash
# yum -y install xrdp tigervnc-server
# systemctl start xrdp.service
# systemctl enable xrdp.service

# vi /etc/xrdp/xrdp.ini
port=8880
# firewall-cmd --permanent --add-port=8880/tcp
# firewall-cmd --reload



# cat /etc/firewalld/zones/public.xml
<?xml version="1.0" encoding="utf-8"?>
<zone>
  <short>Public</short>
  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  <service name="ssh"/>
  <service name="dhcpv6-client"/>
  <port protocol="tcp" port="8880-8889"/>
</zone>

```
