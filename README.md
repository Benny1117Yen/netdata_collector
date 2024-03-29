# Netdata_collector
Collect system info through netdata in python program.
## MQTT publishing 
1. It gets URL = `https://10.144.49.142:19999/api/v1/allmetrics?format=json` which is a REST API for my master PC.
Notes: You can also add hosts like `/host/Moxa` to this API to get the slaves system payloads.
Something like `https://10.144.49.142:19999/host/Moxa/api/v1/allmetrics?format=json`
2. And I implement `5` funcitons to generate different payload like `user_cpu_usage`.
![Functions](https://github.com/P86071244/netdata_collector/blob/master/Functions.png)
3. The execution file has been checked by pylint.
![Pylint MQTT_PUB](https://github.com/P86071244/netdata_collector/blob/master/MQTT_PUB_pylint.png)
## MQTT subsribing
1. It connects localhost, port 1883 with MQTT publishing.
2. And it subscribes five tags.
![Tags](https://github.com/P86071244/netdata_collector/blob/master/MQTT_CLIENT.png)
3. The execution file has been checked by pylint.
![Pylint MQTT_SUB](https://github.com/P86071244/netdata_collector/blob/master/MQTT_SUB_pylint.png)
## Unittest
1. Copy the mqtt_pub.py to the tests directory.
2. Then type `python -m unnittest test_mqtt_pub.py`
3. The result will be like the following figure.
![Unittest_result](https://github.com/P86071244/netdata_collector/blob/master/Unittest_result.png)
