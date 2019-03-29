**mutt usage**
```bash
yum install postfix

cat /etc/postfix/main.cf
#######################################################################
myhostname = mail.sktelecom.com
#######################################################################
mydomain = sktelecom.com
#######################################################################
mynetworks = 58.120.240.170/24
#######################################################################
inet_interfaces = all
#inet_interfaces = localhost
# Enable IPv4, and IPv6 if supported
inet_protocols = all


yum install mutt

cat /home/user/.muttrc
set from = "operation_team@email.com"
set realname = "operation_news"




mutt --help
options:
  -a <file> [...] --    attach file(s) to the message
                the list of files must be terminated with the "--" sequence
  -b <address>  specify a blind carbon-copy (BCC) address
  -c <address>  specify a carbon-copy (CC) address
  -f <file>     specify which mailbox to read
  -s <subj>     specify a subject (must be in quotes if it has spaces)



echo "Hello World!!!" | mutt -s "checking send email using mutt" userid@email.com  -a attach.zip -c username@email.com -b admin@email.com

cat contents
Hello World!!!

mutt -s "checking send email using mutt" userid@email.com  -a attach.zip -c username@email.com -b admin@email.com < contents


```
