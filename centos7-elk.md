**Install elasticsearch**
https://www.elastic.co/kr/downloads/elasticsearch

**1) Download and unzip**
```bash
$ tar -zxvf elasticsearch-7.7.0-linux-x86_64.tar.gz


```

**2) Run bin/elasticsearch**
```bash
$ cd ./elasticsearch* && ./bin/elasticsearch


```


**Install kibana**
https://www.elastic.co/kr/downloads/kibana

**1) Download and unzip**
```bash
$ tar -zxvf kibana-7.7.0-linux-x86_64.tar.gz


```


**Install logstash**
https://www.elastic.co/kr/downloads/logstash

**1) Download and unzip**
```bash
$ tar -zxvf logstash-7.7.0.tar.gz


```


**Auth using x-pack**
https://www.elastic.co/guide/en/kibana/current/using-kibana-with-security.html

**1) Download and unzip**
```bash
$ vi kibana.yml
elasticsearch.username: "kibana_system"
elasticsearch.password: "kibanapassword"

```





