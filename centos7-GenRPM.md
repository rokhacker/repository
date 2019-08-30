**Generate RPM**


**1. install rpmbuild**
```bash
$ yum install rpm-build -y

```


**2. write spec file**
```bash
$ cat hello-world.sh
Name:       hello-world
Version:    0.0.1
Release:    0.0.1
Summary:    hello-world-0.0.1
License:    GPL

%description
hello-world-0.0.1

%prep
# previous step of build

%build
#cat > hello-world.sh <<EOF
##!/bin/sh
#echo
#echo Hello world
#echo
#EOF
cat /tmp/hello-world.sh hello-world.sh

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-world.sh %{buildroot}/usr/bin/hello-world.sh

%files
/usr/bin/hello-world.sh

%changelog
* Fri Aug 30 2019 suser <suser@example.com> - 0.0.1

```
