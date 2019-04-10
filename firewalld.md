**check zone**
```bash
[root@~]# firewall-cmd --get-zones
block dmz drop external home internal public trusted work
[root@~]# firewall-cmd --get-default-zone
public
[root@~]# firewall-cmd --set-default-zone=dmz
success
[root@~]# firewall-cmd --get-default-zone
dmz
[root@~]# firewall-cmd --get-active-zone
public
  interfaces: enp0s25
  sources: 127.0.0.1
[root@~]# cat /etc/firewalld/zones/public.xml
<?xml version="1.0" encoding="utf-8"?>
<zone>
  <short>Public</short>
  <description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
  <source address="127.0.0.1"/>
  <service name="ssh"/>
  <service name="dhcpv6-client"/>
  <port protocol="tcp" port="6000-6063"/>
  <port protocol="tcp" port="8880-8889"/>
</zone>
[root@~]#

```



**add/remove zone**
```bash
#### add/remove zone
[root@~]# firewall-cmd --permanent --new-zone=newzone
[root@~]# firewall-cmd --permanent --delete-zone=newzone

#### pre-defined service lists
[root@~]# firewall-cmd --get-services
RH-Satellite-6 amanda-client amanda-k5-client bacula bacula-client bgp bitcoin bitcoin-rpc bitcoin-testnet bitcoin-testnet-rpc ceph ceph-mon cfengine condor-collector ctdb dhcp dhcpv6 dhcpv6-client dns docker-registry docker-swarm dropbox-lansync elasticsearch freeipa-ldap freeipa-ldaps freeipa-replication freeipa-trust ftp ganglia-client ganglia-master git gre high-availability http https imap imaps ipp ipp-client ipsec irc ircs iscsi-target jenkins kadmin kerberos kibana klogin kpasswd kprop kshell ldap ldaps libvirt libvirt-tls managesieve mdns minidlna mongodb mosh mountd ms-wbt mssql murmur mysql nfs nfs3 nmea-0183 nrpe ntp openvpn ovirt-imageio ovirt-storageconsole ovirt-vmconsole pmcd pmproxy pmwebapi pmwebapis pop3 pop3s postgresql privoxy proxy-dhcp ptp pulseaudio puppetmaster quassel radius redis rpc-bind rsh rsyncd samba samba-client sane sip sips smtp smtp-submission smtps snmp snmptrap spideroak-lansync squid ssh syncthing syncthing-gui synergy syslog syslog-tls telnet tftp tftp-client tinc tor-socks transmission-client upnp-client vdsm vnc-server wbem-https xmpp-bosh xmpp-client xmpp-local xmpp-server zabbix-agent zabbix-server
```


**add/remove port**
```bash
#### add/remove port
[root@~]# firewall-cmd --permanent --zone=public --add-port=8080/tcp
[root@~]# firewall-cmd --permanent --zone=public --add-port=4000-4100/tcp
[root@~]# firewall-cmd --permanent --zone=public --remove-port=8080/tcp
```

**apply at firewalld**
```bash
[root@~]# firewall-cmd --reload
```
