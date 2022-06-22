# learning-logstash-and-elastic-search-plugins
learning logstash and elastic search plugins

## Lab 1:

* create a file sample.conf inside XXXXX\LogStash\logstash-8.2.3\config 
```
input {
  stdin  {
 
  }
}
 
output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "hellodb"
  }
}
```
#### Video : https://www.youtube.com/watch?v=g_s6YK3UxbU

## Lab 2:

* Download Dataset https://download.elastic.co/demos/logstash/gettingstarted/logstash-tutorial.log.gz
* Download File beat : https://www.elastic.co/downloads/beats/filebeat
![image](https://user-images.githubusercontent.com/39345855/175112903-14525bab-490b-45b7-aeaa-f3eefd6ade45.png)
