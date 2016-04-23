import json


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
    path = "/tmp/gps_feed"
    fifo = open(path, "r")

    for line in fifo:
        packet = json.loads(json.dumps(line))
        fifo.close()
        return packet

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
    path = "/tmp/attitude_feed"
    fifo = open(path, "r")

    for line in fifo:
        packet = json.loads(json.dumps(line))
        fifo.close()
        return packet
