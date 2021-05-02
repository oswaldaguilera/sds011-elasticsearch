import sds011

port = "/dev/ttyUSB0"
sds = sds011.SDS011(port=port)
print(sds)