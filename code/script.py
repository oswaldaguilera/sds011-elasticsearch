import sds011

port = "/dev/ttyUSB0"
sds = sds011.SDS011(port=port)
print(sds)
sds.set_working_period(rate=1)

#from elasticsearch import Elasticsearch
#es = Elasticsearch()