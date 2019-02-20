
***source link*** : https://github.com/catonrug/raspbian-zabbix-3/blob/master/server-install.sh

```bash
# install applications
sudo apt-get update -y && apt-get upgrade -y

#you are prompted to enter password here. please enter password [reverse]
apt-get install mysql-client default-libmysqlclient-dev -y
apt-get install apache2 apache2-dev -y
apt-get install php php-dev php-gd php-mysql -y
apt-get install fping -y
apt-get install libiksemel-dev -y
apt-get install libxml2-dev -y
apt-get install libsnmp-dev -y
apt-get install libssh2-1-dev -y
apt-get install libopenipmi-dev -y
apt-get install libcurl4-openssl-dev -y
apt-get install libevent-dev -y
apt-get install libpcre3-dev -y
apt-get install php-bcmath -y
apt-get install php-mbstring -y
apt-get install php-xml -y


# create database
/usr/bin/mysqladmin -u root -preverse password 'zabbix_password'
mysql -h localhost -uroot -pzabbix_password -P 3306 -s <<< 'CREATE DATABASE zabbix CHARACTER SET UTF8'
mysql -h localhost -uroot -pzabbix_password -P 3306 -s <<< 'GRANT ALL PRIVILEGES on zabbix.* to "zabbix"@"localhost" IDENTIFIED BY "zabbix_password"'


# setup account
groupadd zabbix
useradd -g zabbix zabbix
mkdir -p /var/log/zabbix
chown -R zabbix:zabbix /var/log/zabbix/
mkdir -p /var/zabbix/alertscripts
mkdir -p /var/zabbix/externalscripts
chown -R zabbix:zabbix /var/zabbix/


# setup database of zabbix
cd /usr/local/src/
tar -vzxf zabbix-3.4.1.tar.gz
mv zabbix-3.4.1/ /usr/local/
cd /usr/local/zabbix-3.4.1/database/mysql
echo processing schema.sql
time mysql -uzabbix -pzabbix_password zabbix < schema.sql
echo processing images.sql
time mysql -uzabbix -pzabbix_password zabbix < images.sql
echo processing data.sql
time mysql -uzabbix -pzabbix_password zabbix < data.sql


# compile source
cd /usr/local/zabbix-3.4.1/
./configure --enable-server --enable-agent --with-mysql --with-libcurl --with-libxml2 --with-ssh2 --with-net-snmp --with-openipmi --with-jabber=/usr
time make&&make install


# register daemon
cp /usr/local/zabbix-3.4.1/misc/init.d/debian/* /etc/init.d/
update-rc.d zabbix-server defaults
update-rc.d zabbix-agent defaults
update-rc.d zabbix-server enable
update-rc.d zabbix-agent enable



# initiate zabbix_server.conf
sed -i "s/^DBUser=.*$/DBUser=zabbix/" /usr/local/etc/zabbix_server.conf
sed -i "s/^.*DBPassword=.*$/DBPassword=zabbix_password/" /usr/local/etc/zabbix_server.conf
sed -i "s/^.*FpingLocation=.*$/FpingLocation=\/usr\/bin\/fping/" /usr/local/etc/zabbix_server.conf
sed -i "s/^.*AlertScriptsPath=.*$/AlertScriptsPath=\/var\/zabbix\/alertscripts/" /usr/local/etc/zabbix_server.conf
sed -i "s/^.*ExternalScripts=.*$/ExternalScripts=\/var\/zabbix\/externalscripts/" /usr/local/etc/zabbix_server.conf
sed -i "s/^LogFile=.*$/LogFile=\/var\/log\/zabbix\/zabbix_server.log/" /usr/local/etc/zabbix_server.conf
mkdir /var/www/html/zabbix



cd /usr/local/zabbix-3.4.1/frontends/php/
cp * /var/www/html/zabbix/
sed -i "s/^post_max_size = .*$/post_max_size = 16M/" /etc/php/7.2/apache2/php.ini
sed -i "s/^max_execution_time = .*$/max_execution_time = 300/" /etc/php/7.2/apache2/php.ini
sed -i "s/^max_input_time = .*$/max_input_time = 300/g" /etc/php/7.2/apache2/php.ini
sed -i "s/^.*date.timezone =.*$/date.timezone = Europe\/Riga/g" /etc/php/7.2/apache2/php.ini
sed -i "s/^.*always_populate_raw_post_data = .*$/always_populate_raw_post_data = -1/g" /etc/php/7.2/apache2/php.ini,ipaddress=$(ifconfig | grep "inet.*addr.*Bcast.*Mask" | sed "s/  Bcast.*$//g" | sed "s/^.*://g")




cat > /var/www/html/zabbix/conf/zabbix.conf.php << EOF
<?php
// Zabbix GUI configuration file.
global \$DB;
\$DB['TYPE']     = 'MYSQL';
\$DB['SERVER']   = 'localhost';
\$DB['PORT']     = '0';
\$DB['DATABASE'] = 'zabbix';
\$DB['USER']     = 'zabbix';
\$DB['PASSWORD'] = 'zabbix_password';
// Schema name. Used for IBM DB2 and PostgreSQL.
\$DB['SCHEMA'] = '';
\$ZBX_SERVER      = 'localhost';
\$ZBX_SERVER_PORT = '11051';
\$ZBX_SERVER_NAME = '$ipaddress';
\$IMAGE_FORMAT_DEFAULT = IMAGE_FORMAT_PNG;
?>
EOF





#install additional debugging tools
#apt-get install mtr nmap dstat telnet python-mechanize python-requests -y

#reset ip address in config if sd card is moved to another raspberry
cat > /etc/network/if-up.d/zabbix-server-ip << EOF
#!/bin/sh
ipaddress=\$(ifconfig | grep "inet.*addr.*Bcast.*Mask" | sed "s/  Bcast.*\$//g" | sed "s/^.*://g")
sed -i "s/^\\\$ZBX_SERVER_NAME = .*$/\\\$ZBX_SERVER_NAME = \d039\`echo \$ipaddress\`\d039;/" /var/www/html/zabbix/conf/zabbix.conf.php
EOF
chmod +x /etc/network/if-up.d/zabbix-server-ip

```
