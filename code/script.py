
import sds011
import json
from elasticsearch import Elasticsearch



port = "/dev/ttyUSB0"
sds = sds011.SDS011(port=port)
print(sds)
sds.set_working_period(rate=0)
sds.set_data_reporting(mode_select="active")
#meas = sds.query_data()
i = 0
es = Elasticsearch()
while True:
    i=i+1
    meas = sds.read_measurement()
    measJson = {"timestamp" : meas["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
            "pm2.5" : meas["pm2.5"],
            "pm10" : meas["pm10"]
            }
    es.index(index='sds-011-2',id=i,body=meas)
    print(measJson)
