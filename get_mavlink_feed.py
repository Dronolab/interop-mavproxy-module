import json
import socket

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
    sock.bind((self.ip, self.port))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "gps_data:", data
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
    sock.bind((self.ip, self.port))

    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "attitude:", data
        return json.loads(data)
