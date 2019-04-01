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

**boot
$ qemu-system-x86_64 -m 2048 -hda linux.img -boot d



```
