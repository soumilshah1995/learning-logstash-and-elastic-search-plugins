# learning-logstash-and-elastic-search-plugins
learning logstash and elastic search plugins

#### Lab 1:

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
