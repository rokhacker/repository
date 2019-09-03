**Generate RPM**


**1. install rpmbuild**
```bash
$ yum install rpm-build -y

```

**2. write source file**
```bash
$ cat /tmp/hello-world.sh
#!/bin/sh

echo ================
echo hello world
echo ================
```


**3. write spec file**
```bash
$ cat hello-world.spec
Name:       hello-world
Version:    0.0.1
Release:    0.0.1
Summary:    hello-world-0.0.1
License:    GPL

%description
hello-world-0.0.1

%prep
# previous execute of install

%post
# post execute of install

%build
#cat > hello-world.sh <<EOF
##!/bin/sh
#echo
#echo Hello world
#echo
#EOF
cp /tmp/hello-world.sh hello-world.sh

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%preun
# previous execute of uninstall

%postun
# post execute of uninstall
# /sbin/userdel -r suser
# /bin/rm -rf /etc/suser.tmp

%changelog
* Fri Aug 30 2019 suser <suser@example.com> - 0.0.1
- Initial RPM release
```


**4. build to RPM**
This step occurs errors below but make rpmbuild directory.
```bash
]$ rpmbuild -ba hello-world.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.dXYgjQ
+ umask 022
+ cd /home/suser/rpmbuild/BUILD
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.E9gIaA
+ umask 022
+ cd /home/suser/rpmbuild/BUILD
+ gcc -o hello-world /tmp/hello-world.c
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.9Np5Uk
+ umask 022
+ cd /home/suser/rpmbuild/BUILD
+ '[' /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64 '!=' / ']'
+ rm -rf /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64
++ dirname /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64
+ mkdir -p /home/suser/rpmbuild/BUILDROOT
+ mkdir /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64
+ mkdir -p /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64/usr/bin/
+ install -m 755 hello-world /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64/usr/bin/hello-world
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip /usr/bin/strip
+ /usr/lib/rpm/redhat/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: hello-world-0.0.1-0.0.1.x86_64
Provides: hello-world = 0.0.1-0.0.1 hello-world(x86-64) = 0.0.1-0.0.1
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: libc.so.6()(64bit) libc.so.6(GLIBC_2.2.5)(64bit) rtld(GNU_HASH)
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64
Wrote: /home/suser/rpmbuild/SRPMS/hello-world-0.0.1-0.0.1.src.rpm
Wrote: /home/suser/rpmbuild/RPMS/x86_64/hello-world-0.0.1-0.0.1.x86_64.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.sz4HQC
+ umask 022
+ cd /home/suser/rpmbuild/BUILD
+ /usr/bin/rm -rf /home/suser/rpmbuild/BUILDROOT/hello-world-0.0.1-0.0.1.x86_64
+ exit 0
$
```



**5. using RPM**
This step occurs errors below but make rpmbuild directory.
```bash
$ cd rpmbuild/RPMS/x86_64/
$ ls
hello-world-0.0.1-0.0.1.x86_64.rpm
$ sudo rpm -ivh hello-world-0.0.1-0.0.1.x86_64.rpm
Preparing...                          ################################# [100%]
Updating / installing...
   1:hello-world-0.0.1-0.0.1          ################################# [100%]
[suser@mojave x86_64]$ hello-world
================
hello world
================

$

$ sudo rpm -e hello-world
$ hello-world
bash: hello-world: command not found...
$

```
