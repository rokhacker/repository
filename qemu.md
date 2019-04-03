**qemu**
```bash
**file info
$ qemu-img info linux.img
image: linux.img
file format: qcow2
virtual size: 20G (21474836480 bytes)
disk size: 14G
cluster_size: 65536
Format specific information:
    compat: 0.10
    refcount bits: 16
$

**Can't get ip
mv /etc/udev/rules.d/70-persistent-net.rules /etc/udev/rules.d/70-persistent-net.rules.bak
reboot

**boot for console only
$ qemu-system-x86_64 -m 2048 -hda linux.img -boot d

## Port Forwarding option
-net nic -net user,hostfwd=tcp::2222-:22,hostfwd=tcp::1443-:443,hostfwd=tcp::8080-:80

## connection
$ ssh user@localhost -p2222
$ curl http://localhost:8080

```
