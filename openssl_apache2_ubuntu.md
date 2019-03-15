***# source link*** : https://www.digitalocean.com/community/tutorials/how-to-create-a-ssl-certificate-on-apache-for-debian-8

```bash
# Step 1 — Install Apache
apt-get install apache2


# Step 2 — Enable the SSL Module
# First, enable the Apache SSL module.
a2enmod ssl

# The default Apache website comes with a useful template for enabling SSL, so we will activate the default website now.
a2ensite default-ssl

# Restart Apache to put these changes into effect.
service apache2 reload


# Step 3 — Create a Self-Signed SSL Certificate
# First, let's create a new directory where we can store the private key and certificate.
mkdir /etc/apache2/ssl


# Next, we will request a new certificate and sign it.

# First, generate a new certificate and a private key to protect it.

# The days flag specifies how long the certificate should remain valid. With this example, the certificate will last for one year
# The keyout flag specifies the path to our generated key
# The out flag specifies the path to our generated certificate
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/apache2/ssl/apache.key -out /etc/apache2/ssl/apache.crt


# Example answers are shown in red below.

# Interactive
# You are about to be asked to enter information that will be incorporated
# into your certificate request.
# What you are about to enter is what is called a Distinguished Name or a DN.
# There are quite a few fields but you can leave some blank
# For some fields there will be a default value,
# If you enter '.', the field will be left blank.
# ——-
# Country Name (2 letter code) [AU]:US
# State or Province Name (full name) [Some-State]:New York
# Locality Name (eg, city) []:NYC
# Organization Name (eg, company) [Internet Widgits Pty Ltd]:DigitalOcean
# Organizational Unit Name (eg, section) []:SSL Certificate Test
# Common Name (e.g. server FQDN or YOUR name) []:example.com               
# Email Address []:test@example.com



# Set the file permissions to protect your private key and certificate.
chmod 600 /etc/apache2/ssl/*




# Step 4 — Configure Apache to Use SSL
# In this section, we will configure the default Apache virtual host to use the SSL key and certificate. 
# After making this change, our server will begin serving HTTPS instead of HTTP requests for the default site.

vi /etc/apache2/sites-enabled/default-ssl.conf

# Locate the section that begins with <VirtualHost _default_:443> and make the following changes.
# Add a line with your server name directy below the ServerAdmin email line. This can be your domain name or IP address:
# ------------------------------------------------------------------
 ServerAdmin webmaster@localhost
 ServerName example.com:443
# ------------------------------------------------------------------
# Find the following two lines, and update the paths to match the locations of the certificate and key we generated earlier. 
# If you purchased a certificate or generated your certificate elsewhere, 
# make sure the paths here match the actual locations of your certificate and key:
# ------------------------------------------------------------------
 SSLCertificateFile /etc/apache2/ssl/apache.crt
 SSLCertificateKeyFile /etc/apache2/ssl/apache.key
# ------------------------------------------------------------------
# Once these changes have been made, check that your virtual host configuration file matches the following.

# ------------------------------------------------------------------
<IfModule mod_ssl.c>
    <VirtualHost _default_:443>
        ServerAdmin webmaster@localhost
        ServerName example.com:443
        DocumentRoot /var/www/html

        . . .
        SSLEngine on

        . . .

        SSLCertificateFile /etc/apache2/ssl/apache.crt
        SSLCertificateKeyFile /etc/apache2/ssl/apache.key
# ------------------------------------------------------------------
# Save and exit the file.

# Restart Apache to apply the changes.
service apache2 reload



# Step 5 — Test Apache with SSL
```
