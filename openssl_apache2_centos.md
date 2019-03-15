***# source link*** : https://www.digitalocean.com/community/tutorials/how-to-create-an-ssl-certificate-on-apache-for-centos-7

```bash
yum -y install apache2

# Step 1 : install mod_ssl
yum install mod_ssl


# Step 2 : create a new certificate

mkdir /etc/ssl/private
chmod 700 /etc/ssl/private
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt

openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048
cat /etc/ssl/certs/dhparam.pem | sudo tee -a /etc/ssl/certs/apache-selfsigned.crt


# Step 3 : setup certificate
vi /etc/httpd/conf.d/ssl.conf
<VirtualHost _default_:443>
. . .
DocumentRoot "/var/www/example.com/public_html"
ServerName www.example.com:443
.
.
# SSLProtocol all -SSLv2
. . .
# SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5:!SEED:!IDEA
.
.
SSLCertificateFile /etc/ssl/certs/apache-selfsigned.crt
SSLCertificateKeyFile /etc/ssl/private/apache-selfsigned.key



##### Begin copied text
</VirtualHost>
. . .

# from https://cipherli.st/
# and https://raymii.org/s/tutorials/Strong_SSL_Security_On_Apache2.html

SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
SSLProtocol All -SSLv2 -SSLv3
SSLHonorCipherOrder On
# Disable preloading HSTS for now.  You can use the commented out header line that includes
# the "preload" directive if you understand the implications.
#Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains; preload"
Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains"
Header always set X-Frame-Options DENY
Header always set X-Content-Type-Options nosniff
# Requires Apache >= 2.4
SSLCompression off 
SSLUseStapling on 
SSLStaplingCache "shmcb:logs/stapling-cache(150000)" 
# Requires Apache >= 2.4.11
# SSLSessionTickets Off


apachectl configtest

systemctl restart httpd.service



```
