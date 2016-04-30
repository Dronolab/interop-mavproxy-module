import json
import socket

# Receiving IP
ip = "127.0.0.1"

# Receiving port
port = 5006

#
# Will return a dict containing the following properties:
#
#   packet_id
#   time_boot_ms
#   lat
#   lon
#   alt
#   relative_alt
#   vx
#   vy
#   vz
#   hdg
#
def get_gps_data():
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
        #print "gps_data:", data
	if(json.loads(data)['packet_id'] != 33):
		continue
        return json.loads(data)


#
# Will return a dict containing the following properties
#
#   packet_id
#   time_boot_ms
#   roll
#   pitch
#   yaw
#   rollspeed
#   pitchspeed
#   yawspeed
#
def get_attitude():
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((ip, port))

    while True:
        data, addr = sock.recvfrom(2048) # buffer size is 1024 bytes
        #print "attitude:", data
        if(json.loads(data)['packet_id'] != 30):
                continue
        return json.loads(data)
