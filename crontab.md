
**Best important two point of crontab**

**1) PATH**
Starting path is basic path.
For example, path is / or /root on cron of root. and path is /home/user on cron of user.

```bash
1. Set full Path
Good Case
* * * * * /bin/grep string $(/bin/cat /usr/local/app/start.sh)
* * * * * cd /usr/local/app/; /bin/grep string $(/bin/sh start.sh)

Not Good Case
* * * * * grep string $(cat /usr/local/app/start.sh)
* * * * * /bin/grep string $(/bin/sh start.sh)

```


**2) ENVIRONMENT**

```bash
* * * * * source /home/user/.bash_profile; /bin/grep string $(/bin/sh /usr/local/app/start.sh)


```
