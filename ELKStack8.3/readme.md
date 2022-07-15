

-------------------

Step 1: Install 
----------------------


		https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.3.2-windows-x86_64.zip

		https://artifacts.elastic.co/downloads/kibana/kibana-8.3.2-windows-x86_64.zip				

		https://artifacts.elastic.co/downloads/logstash/logstash-8.3.2-windows-x86_64.zip

----------------------------------------------------------------------------------------


---------------------------

Step 2: Unzip 
----------------------------



-----------------------------------

Step 3: Installation Steps
--------------------------------------
		https://www.elastic.co/guide/en/elasticsearch/reference/current/zip-windows.html

----------------------------------------------------------------------------------------





--------------------------------------
Step 4: After Unzip 

--------------------------------------

		Add this line in elasticsearch.yml file 
		action.auto_create_index: .monitoring*,.watches,.triggered_watches,.watcher-history*,.ml*
		
		Start the Elastic search 
		elasticsearch.bat

		Once you see Token press CTR + C and stop it and copy Paste TOKEN 
		
		Open elasticsearc.yml file again 
		
		***********
		
		SET this to false 
		enabled: true
		
		*************
		
		xpack.security.http.ssl:
		  enabled: false
		  keystore.path: certs/http.p12
		
		xpack.security.transport.ssl:
		  enabled: false
		  verification_mode: certificate
		  keystore.path: certs/transport.p12
		  truststore.path: certs/transport.p12
		  
		  
		Start elastic search 
		
		elasticsearch.bat
		
----------------------------------------------------------------------------------------


--------------------------------------
Step 5: Reset passwords for Elastic User and kibana system 
--------------------------------------

		
		
		GO TO BIN directory and OPEN CMD 
		
		elasticsearch-reset-password -u elastic
		
		elasticsearch-reset-password -u kibana_system
		
		NOTE THE PASS ON NOTEPAD
		
--------------------------------------



--------------------------------------
Step 6: Logstash conf file 
--------------------------------------

	input {
	  stdin  {
	 
	  }
	}
	 
	output {

	 stdout {
		codec => rubydebug
	  }
	  
	  elasticsearch {
		hosts => ["http://localhost:9200"]
		index => "test.logstash"
		user => "elastic"
		password => "XXXXXXXXXXXXXXXX"
		
	  }
}


---------------
ENJOY 
-------------

