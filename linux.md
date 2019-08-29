**sudo command is so slow on terminal**
```bash
$ hosname
home

Add your hostname & ip
$ cat /etc/hosts
127.0.0.1 localhost home
$
```

**Edit System Service**
```bash
systemctl enable elasticsearch
systemctl list-unit-files | grep elasticsearch
elasticsearch.service                         enabled

systemctl start elasticsearch
systemctl status elasticsearch
systemctl stop elasticsearch


```


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
# firewall-cmd --zone=public --permanent --add-port=8880-8889/tcp
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



**setup APM on CentOS 7**
```bash
yum install libjpeg* libpng* freetype* gd-* gcc gcc-c++ gdbm-devel libtermcap-devel

####################################################################
yum install httpd
####################################################################
## setting new repository for php 7 because of default version is php 5
rpm -qa | grep php
yum remove php-*

rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm

yum install php70w
yum install php70w-mysql php70w-pdo php70w-pgsql php70w-odbc php70w-mbstring php70w-mcrypt php70w-gd
yum install php70w-pear php70w-pdo_dblib php70w-pecl-imagick php70w-pecl-imagick-devel php70w-xml php70w-xmlrpc
####################################################################
vi /etc/httpd/conf/httpd.conf

Listen 8888

User nobody
Group nobody

ServerName 127.0.0.1:8888

<IfModule dir_module>
        DirectoryIndex index.html index.htm index.php
</IfModule>

#AddType application/x-gzip .tgz
AddType application/x-httpd-php .php .html .htm .inc
AddType application/x-httpd-php-source .phps

<VirtualHost *:8888>
    ServerAdmin admin@localhost
    DocumentRoot /var/www/html
</VirtualHost>

####################################################################
cat /var/www/html/index.php
<?php phpinfo(); ?>
####################################################################
systemctl start httpd
Job for httpd.service failed because the control process exited with error code. See "systemctl status httpd.service" and "journalctl -xe" for details.


systemctl status httpd.service

httpd[1968]: (13)Permission denied: AH00072: make_sock: could not bind to address [::]:8888
httpd[1968]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:8888

setenforce 0
systemctl start httpd
setenforce 1

ps -ef|grep httpd
root      2860     1  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
apache    2862  2860  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
apache    2863  2860  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
apache    2864  2860  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
apache    2866  2860  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND
apache    2868  2860  0 12:47 ?        00:00:00 /usr/sbin/httpd -DFOREGROUND

####################################################################
## For auto start during reboot
####################################################################
semanage port -l | grep http
http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000

semanage port -m -t http_port_t -p tcp 8881
ValueError: Port @tcp/8881 is not defined

semanage port -a -t http_port_t -p tcp 8881
semanage port -a -t http_port_t -p tcp 8880-8889
semanage port -l | grep http
http_port_t                    tcp      8881, 80, 81, 443, 488, 8008, 8009, 8443, 9000

systemctl start httpd
####################################################################



####################################################################
cat /etc/yum.repos.d/MariaDB.repo
[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.1/centos7-amd64
gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1


yum install MariaDB-server MariaDB-client
####################################################################
mysql_secure_installation


####################################################################
## setup openssl
####################################################################
yum install mod_ssl openssl

mkdir /etc/httpd/ssl; cd /etc/httpd/ssl

openssl genrsa -out server.key 2048

openssl req -new -key server.key -out server.csr

openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt


```


**setup basic auth of apache on CentOS 7**
```bash
vi  /etc/httpd/conf.d/ssl.conf
<Directory /var/www/html/>
    AuthType Basic
    AuthName "Hello World!!! Authentication Only!!!"
    AuthUserFile /etc/httpd/conf/.htpasswd
    require valid-user
</Directory>


htpasswd -c /etc/httpd/conf/.htpasswd user_account
New password:
Re-type new password:
cat /etc/httpd/conf/.htpasswd
suser:$apr1$yUzvD0IO$4/KkYmasuVdfYBTAM3s.0N.

apachectl configtest
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 192.168.0.15. Set the 'ServerName' directive globally to suppress this message
Syntax OK

systemctl restart httpd

```


