**1. install crash, kernel-debuginfo, kernel-debuginfo-common-x86_64**  
[+] crash :: analyzer tool  
[+] kernel-debuginfo :: debug module using analyzing  
```bash
# yum install crash
# yum --enablerepo=base-debuginfo install -y kernel-debuginfo-$(uname -r)
.
.
Downloading packages:
warning: /var/cache/yum/x86_64/7/base-debuginfo/packages/kernel-debuginfo-common-x86_64-3.10.0-862.14.4.el7.x86_64.rpm: Header V3 RSA/SHA256 Signature, key ID b6792c39: NOKEY
Public key for kernel-debuginfo-common-x86_64-3.10.0-862.14.4.el7.x86_64.rpm is not installed
(1/2): kernel-debuginfo-common-x86_64-3.10.0-862.14.4.el7.x86_64.rpm                                                             |  57 MB  00:00:59
(2/2): kernel-debuginfo-3.10.0-862.14.4.el7.x86_64.rpm
.
.
```

**2. check version of vmcore file**  
[+] need to have same version of vmcore on os  
```bash
# strings ./vmcore|grep "Linux version"
Linux version 3.10.0-327.el7.x86_64 (mockbuild@x86-034.
# yum --enablerepo=base-debuginfo remove -y kernel-debuginfo-$(uname -r)

```
[+]


**3. check available version**  
```bash
# yum --enablerepo=*-debuginfo --showduplicates list kernel kernel-devel kernel-debuginfo
kernel-debuginfo.x86_64                                               3.10.0-957.1.3.el7                                                 @base-debuginfo
kernel-devel.x86_64                                                   3.10.0-693.el7                                                     @tidcrepo
kernel-devel.x86_64                                                   3.10.0-693.21.1.el7                                                @updates
kernel-devel.x86_64                                                   3.10.0-862.9.1.el7                                                 @updates
kernel-devel.x86_64                                                   3.10.0-862.11.6.el7                                                @updates
kernel-devel.x86_64                                                   3.10.0-862.14.4.el7                                                @updates
Available Packages
kernel.x86_64                                                         3.10.0-862.el7                                                     tidcrepo
kernel.x86_64                                                         3.10.0-957.el7                                                     base
kernel.x86_64                                                         3.10.0-957.1.3.el7                                                 updates
kernel-debuginfo.x86_64                                               3.10.0-123.el7                                                     base-debuginfo
kernel-debuginfo.x86_64                                               3.10.0-957.el7                                                     base-debuginfo
kernel-debuginfo.x86_64                                               3.10.0-957.1.3.el7                                                 base-debuginfo
kernel-devel.x86_64                                                   3.10.0-862.el7                                                     tidcrepo
kernel-devel.x86_64                                                   3.10.0-957.el7                                                     base
kernel-devel.x86_64                                                   3.10.0-957.1.3.el7                                                 updates
```

**4. usage of crash**  
[+] crash [module of vmlinux] [vmcore]  
```bash
# crash /usr/lib/debug/lib/modules/3.10.0-862.14.4.el7.x86_64/vmlinux ./vmcore
```
